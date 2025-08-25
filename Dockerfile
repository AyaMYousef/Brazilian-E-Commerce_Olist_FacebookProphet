# ---- Base ----
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# System deps (build tools for prophet/cmdstan, and basics)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl git ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 appuser
WORKDIR /app

# ---- Python deps ----
# Copy only requirements first for better build caching
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Pre-install CmdStan so Prophet works at runtime
# (avoids first-run compilation/download delays)
RUN python - <<'PY'
import cmdstanpy
cmdstanpy.install_cmdstan()  # downloads & compiles CmdStan inside the image
print("CmdStan installed at:", cmdstanpy.cmdstan_path())
PY

# ---- App code ----
# Copy the rest of the repo
COPY . /app

# Switch to non-root
USER appuser

# Expose FastAPI port
ENV PORT=8000
EXPOSE 8000

# NOTE: README shows entrypoint as `src.main:app`
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
