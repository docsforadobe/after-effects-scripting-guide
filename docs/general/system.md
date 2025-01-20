# System object

`system`

#### Description

The System object provides access to attributes found on the user's system, such as the user name and the name and version of the operating system. It is available through the `system` global variable.

#### Example

```javascript
alert("Your OS is " + system.osName + " running version" + system.osVersion);
confirm("You are: " + system.userName + " running on " + system.machineName + ".");
```

---

## Attributes

### System.machineName

`system.machineName`

#### Description

The name of the computer on which After Effects is running.

#### Type

String; read-only.

---

### System.osName

`system.osName`

#### Description

The name of the operating system on which After Effects is running.

!!! warning
    As of Windows 7, this attribute returns a blank value. Use $.os instead.

#### Type

String; read-only.

---

### System.osVersion

`system.osVersion`

#### Description

The version of the current local operating system.

#### Type

String; read-only.

---

### System.userName

`system.userName`

#### Description

The name of the user currently logged on to the system.

#### Type

String; read-only.

---

## Methods

### System.callSystem()

`system.callSystem(cmdLineToExecute);`

#### Description

Executes a system command, as if you had typed it on the operating system's command line. Returns whatever the system outputs in response to the command, if anything. In Windows, you can invoke commands using the `/c` switch for the `cmd.exe` command, passing the command to run in escaped quotes (`\"...\"`). For example, the following retrieves the current time and displays it to the user:

```javascript
var timeStr = system.callSystem("cmd.exe /c \"time /t\"");
alert("Current time is " + timeStr);
```

#### Parameters

|     Parameter      |  Type  |           Description           |
| ------------------ | ------ | ------------------------------- |
| `cmdLineToExecute` | String | The command and its parameters. |

#### Returns

The output from the command.
