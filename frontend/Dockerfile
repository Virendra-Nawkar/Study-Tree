# ─────────────────────────────────────────
# STAGE 1: Build the React app
# ─────────────────────────────────────────
FROM node:20-alpine AS builder

# Set working directory inside the container
WORKDIR /app

# Copy only package files first (for Docker layer caching)
COPY package.json package-lock.json ./

# Install all dependencies
RUN npm ci

# Copy the rest of the frontend source code
COPY . .

# Build the React app into static files (output goes to /app/build)
RUN npm run build

# ─────────────────────────────────────────
# STAGE 2: Serve with Nginx
# ─────────────────────────────────────────
FROM nginx:alpine

# Copy the built React files from Stage 1 into Nginx's serving directory
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80 so the container can receive HTTP traffic
EXPOSE 80

# Start Nginx in the foreground (containers must have a foreground process)
CMD ["nginx", "-g", "daemon off;"]