$path="C:\Users\andre\OneDrive\Desktop\Tirocinio\Indexes\LogWorkshop\EmailEvents_Logs.txt"
 
$content = Get-content -Path $path 
 
$Body = $content | ConvertTo-Json
 
 
 
$CustomerId = "hidden"
$SharedKey = "hidden"


$StringToSign = "POST" + "`n" + $Body.Length + "`n" + "application/json" + "`n" + $("x-ms-date:" + [DateTime]::UtcNow.ToString("r")) + "`n" + "/api/logs"
$BytesToHash = [Text.Encoding]::UTF8.GetBytes($StringToSign)
$KeyBytes = [Convert]::FromBase64String($SharedKey)
$HMACSHA256 = New-Object System.Security.Cryptography.HMACSHA256
$HMACSHA256.Key = $KeyBytes
$CalculatedHash = $HMACSHA256.ComputeHash($BytesToHash)
$EncodedHash = [Convert]::ToBase64String($CalculatedHash)
$Authorization = 'SharedKey {0}:{1}' -f $CustomerId, $EncodedHash
 
 
 
$Uri = "https://" + $CustomerId + ".ods.opinsights.azure.com" + "/api/logs" + "?api-version=2016-04-01"
$Headers = @{
    "Authorization"        = $Authorization;
    "Log-Type"             = "EmailEvents_1";
    "x-ms-date"            = [DateTime]::UtcNow.ToString("r");
    "time-generated-field" = $(Get-Date)
}
$Response = Invoke-WebRequest -Uri $Uri -Method Post -ContentType "application/json" -Headers $Headers -Body $Body -UseBasicParsing
if ($Response.StatusCode -eq 200) {
    Write-Information -MessageData "Logs are Successfully Stored in Log Analytics Workspace" -InformationAction Continue
} 
