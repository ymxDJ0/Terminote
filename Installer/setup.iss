[Setup]
AppName=Terminote
AppVersion=1.0
DefaultDirName={autopf}\Terminote
DefaultGroupName=Terminote
OutputDir=Output
OutputBaseFilename=Terminote-Installer
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin

[Files]
; Copy your compiled terminote.exe into the destination folder
Source: "..\PyInstallerBuild\dist\terminote.exe"; DestDir: "{app}"; Flags: ignoreversion

[Code]
const
  EnvironmentKey = 'Environment';

procedure ModPath(Path: string);
var
  OldPath: string;
begin
  { Read current user or system path and append your app directory if not already present }
  if RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'Path', OldPath) then
  begin
    if Pos(';' + Path + ';', ';' + OldPath + ';') = 0 then
    begin
      RegWriteStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'Path', OldPath + ';' + Path);
    end;
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    { Automatically adds the installation folder to the Windows System PATH }
    ModPath(ExpandConstant('{app}'));
  end;
end;