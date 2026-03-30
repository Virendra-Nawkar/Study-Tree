# ─────────────────────────────────────────
# STAGE 1: Install dependencies
# ─────────────────────────────────────────
FROM node:20-alpine AS deps

WORKDIR /app

# Copy only package files first (layer cache optimization)
COPY package.json package-lock.json ./

# Install only production dependencies (no devDependencies like nodemon)
RUN npm ci --omit=dev

# ─────────────────────────────────────────
# STAGE 2: Run the app
# ─────────────────────────────────────────
FROM node:20-alpine

WORKDIR /app

# Install ffmpeg system package (required by fluent-ffmpeg dependency)
RUN apk add --no-cache ffmpeg

# Copy production node_modules from Stage 1
COPY --from=deps /app/node_modules ./node_modules

# Copy all backend source code
COPY . .

# Expose the port your Express server listens on
EXPOSE 5000

# Start the server
CMD ["node", "server.js"]