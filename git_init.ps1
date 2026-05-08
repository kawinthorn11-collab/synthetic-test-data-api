# Initializing Git Repository
Write-Host "Navigating to project directory..."
Set-Location -Path "C:\Users\kawinthorn11\Desktop\AssetScanner\synthetic_data_api"

Write-Host "Initializing Git..."
git init

Write-Host "Adding files to staging area..."
git add .

Write-Host "Creating initial commit..."
git commit -m "Initial commit: Synthetic Data API ready for Vercel deployment"

Write-Host ""
Write-Host "=========================================================="
Write-Host "SUCCESS: Local Git repository initialized and committed."
Write-Host "=========================================================="
Write-Host "Next Steps for Deployment:"
Write-Host "1. Create a new empty repository on GitHub (https://github.com/new)"
Write-Host "2. Run the following commands in your terminal to link and push:"
Write-Host "   git branch -M main"
Write-Host "   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git"
Write-Host "   git push -u origin main"
Write-Host "3. Log into Vercel (https://vercel.com) and import the repository."
Write-Host "=========================================================="
