# Generate unique test data
$registerBody = @{
    nombre = "Test User"
    correo = "test.user1112@example.com"
    telefono = "123453452"
    dni = "12345671B"
    password = "testpass123"
} | ConvertTo-Json

Write-Host "Testing Register with data:" -ForegroundColor Green
$registerBody | ConvertFrom-Json | Format-List

try {
    $registerResponse = Invoke-WebRequest `
        -Uri "http://127.0.0.1:8000/api/v1/auth/register" `
        -Method Post `
        -Body $registerBody `
        -ContentType "application/json"
    
    Write-Host "`nRegister successful!" -ForegroundColor Green
    $registerResponse.Content | ConvertFrom-Json | ConvertTo-Json
} catch {
    Write-Host "`nRegister failed:" -ForegroundColor Red
    $_.ErrorDetails.Message
}