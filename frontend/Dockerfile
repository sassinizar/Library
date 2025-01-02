# Use an official Node.js runtime as the base image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire application source code
COPY . .

# Install a lightweight HTTP server to serve static files
RUN npm install -g serve

# Expose the application on port 3000
EXPOSE 3000

# Command to serve the application
CMD ["npm", "start"]
