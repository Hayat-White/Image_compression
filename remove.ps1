# Get the current directory
$CurrentDirectory = Get-Location

# Find files with "converted" or "reconverted" in their names
$FilesToDelete = Get-ChildItem -Path $CurrentDirectory -File | Where-Object {
    $_.Name -match "converted" -or $_.Name -match "reconverted"
}

# Delete the matching files
foreach ($File in $FilesToDelete) {
    Remove-Item -Path $File.FullName -Force
    Write-Host "Deleted: $($File.FullName)"
}
