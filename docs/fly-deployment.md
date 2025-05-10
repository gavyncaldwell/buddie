# Deploying Buddie to fly.io

This guide explains how to deploy the Buddie application to fly.io.

## Prerequisites

1. Install the flyctl CLI:

   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. Log in to fly.io:
   ```bash
   fly auth login
   ```

## Manual Deployment

To deploy the application manually:

1. Launch the application (first time only):

   ```bash
   fly launch
   ```

   This will ask a few questions and create a `fly.toml` file.

2. Create a PostgreSQL database (first time only):

   ```bash
   fly postgres create --name buddie-db
   ```

3. Attach the database to your app:

   ```bash
   fly postgres attach --app buddie buddie-db
   ```

4. Deploy the application:
   ```bash
   fly deploy
   ```

## GitHub Actions Deployment

To set up automatic deployments via GitHub Actions:

1. Create a fly.io API token:

   ```bash
   fly auth token
   ```

2. Add the token as a GitHub secret:

   - Go to your GitHub repository
   - Click on "Settings" > "Secrets and variables" > "Actions"
   - Click "New repository secret"
   - Name: `FLY_API_TOKEN`
   - Value: [paste the token from step 1]

3. Push to the `main` branch to trigger the deployment workflow

## Environment Variables

Set environment variables on fly.io:

```bash
fly secrets set SECRET_KEY=your_secret_key
fly secrets set OAUTH_GOOGLE_CLIENT_ID=your_client_id
fly secrets set OAUTH_GOOGLE_CLIENT_SECRET=your_client_secret
```

## Monitoring and Logs

View logs:

```bash
fly logs
```

Check app status:

```bash
fly status
```

Open the app in a browser:

```bash
fly open
```
