# ─────────────────────────────────────────
# STAGE 1: Install dependencies
# ─────────────────────────────────────────
FROM node:20-slim AS deps

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --omit=dev

# ─────────────────────────────────────────
# STAGE 2: Run the app
# ─────────────────────────────────────────
FROM node:20-slim

WORKDIR /app

# Install ffmpeg, python3, pip, yt-dlp and whisper
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg python3 python3-pip python3-setuptools curl && \
    pip3 install --no-cache-dir --break-system-packages "yt-dlp[default]" whisper-ctranslate2 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=deps /app/node_modules ./node_modules
COPY . .

EXPOSE 5000
CMD ["node", "server.js"]