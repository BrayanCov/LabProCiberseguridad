function Menu{
    do 
    {   
         cls
         Write-Host "<<|-- Menú --|>>>"
         Write-Host "1.-Ver la IP de mi equipo y de la puerta de conexión"
         Write-Host "2.-Ver las conexiones TCP del equipo"
         Write-Host "3.-Perfil de red actual"
         write-Host "4.-Salir"
         $opcion = Read-Host "Elegir una opcion: " 
         cls
         switch ($opcion) 
         { 
               
               '1' { 
                        $var1 = Get-NetIPConfiguration -InterfaceAlias "Wi-Fi"
                        Write-Host "La IP del equipo es:" $var1.IPv4Address.IPAddress
                        Write-Host "La Ip del modem es:" $var1.IPv4DefaultGateway.NextHop
                    } 
               '2' {  
                        Get-NetTCPConnection | Format-Table -AutoSize
                    } 
               '3' {
                        $perfilRed = Get-NetConnectionProfile  
                        Write-Host "Nombre de red:" $perfilRed.Name
                        Write-Host "Perfil de red:" $perfilRed.NetworkCategory  
                    } 
               
               '4' {
                        Write-Host "Saliendo..."
                        #return
               }
               default{
                        Write-Host "Opción no valida"
               }
         } 
         pause
         cls
    } 
    until ($opcion -eq '4')
}
Menu