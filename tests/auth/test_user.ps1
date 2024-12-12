# Login to get token
$loginBody = @{
    username = "test.user1112@example.com"
    password = "testpass123"
}

Write-Host "1. Getting auth token..." -ForegroundColor Cyan
try {
    $loginResponse = Invoke-WebRequest `
        -Uri "http://127.0.0.1:8000/api/v1/auth/login" `
        -Method Post `
        -Body $loginBody `
        -ContentType "application/x-www-form-urlencoded"
    
    $token = ($loginResponse.Content | ConvertFrom-Json).access_token
    Write-Host "Token obtained successfully" -ForegroundColor Green
} catch {
    Write-Host "Login failed:" -ForegroundColor Red
    $_.ErrorDetails.Message
    exit 1
}

$headers = @{
    "Authorization" = "Bearer $token"
}

# Test /me endpoint without decryption
Write-Host "`n2. Testing /me endpoint (Encrypted)..." -ForegroundColor Cyan
try {
    $meResponse = Invoke-WebRequest `
        -Uri "http://127.0.0.1:8000/api/v1/auth/user/me" `
        -Method Get `
        -Headers $headers
    
    Write-Host "`nEncrypted Response:" -ForegroundColor Yellow
    $meResponse.Content | ConvertFrom-Json | ConvertTo-Json
} catch {
    Write-Host "`nEncrypted request failed:" -ForegroundColor Red
    $_.ErrorDetails.Message
}

# Test /me endpoint with decryption
Write-Host "`n3. Testing /me endpoint (Decrypted)..." -ForegroundColor Cyan
try {
    $meDecryptedResponse = Invoke-WebRequest `
        -Uri "http://127.0.0.1:8000/api/v1/auth/user/me?desencriptar=true" `
        -Method Get `
        -Headers $headers
    
    Write-Host "`nDecrypted Response:" -ForegroundColor Green
    $meDecryptedResponse.Content | ConvertFrom-Json | ConvertTo-Json
} catch {
    Write-Host "`nDecrypted request failed:" -ForegroundColor Red
    $_.ErrorDetails.Message
}