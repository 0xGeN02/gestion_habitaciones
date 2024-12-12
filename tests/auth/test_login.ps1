# Login credentials
$loginBody = @{
    username = "test.user1112@example.com"  # Use email from registration
    password = "testpass123"                # Use password from registration
}

Write-Host "Testing Login with credentials:" -ForegroundColor Green
$loginBody | Format-List

try {
    $loginResponse = Invoke-WebRequest `
        -Uri "http://127.0.0.1:8000/api/v1/auth/login" `
        -Method Post `
        -Body $loginBody `
        -ContentType "application/x-www-form-urlencoded"
    
    Write-Host "`nLogin successful!" -ForegroundColor Green
    Write-Host "Response:" -ForegroundColor Yellow
    $loginResponse.Content | ConvertFrom-Json | ConvertTo-Json

    # Extract and store token
    $token = ($loginResponse.Content | ConvertFrom-Json).access_token
    Write-Host "`nAccess Token:" -ForegroundColor Cyan
    Write-Host $token
} catch {
    Write-Host "`nLogin failed:" -ForegroundColor Red
    $_.ErrorDetails.Message
}