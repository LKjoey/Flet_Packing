# Flet_App_Packing
用来打包 flet 应用至各个平台


| File Name                                                    | Builds                                                       | Runs on                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------- |
| [aab-build.yml](.github/workflows/aab-build.yml)             | Android App Bundle (AAB)                                     | ubuntu-latest                               |
| [apk-build.yml](.github/workflows/apk-build.yml)             | Android Application Package (APK)                            | ubuntu-latest                               |
| [desktop-and-mobile-builds.yml](.github/workflows/desktop-and-mobile-builds.yml) | desktop [linux, macOS, windows] and mobile [Android (AAB, APK), iOS (IPA)] apps | ubuntu-latest, macos-latest, windows-latest |
| [desktop-build.yml](.github/workflows/desktop-builds.yml)    | desktop [Linux, macOS, windows] apps                         | ubuntu-latest, macos-latest, windows-latest |
| [ipa-build.yml](.github/workflows/ipa-build.yml)             | iOS Package App Store (IPA)                                  | macos-latest                                |
| [linux-build.yml](.github/workflows/linux-build.yml)         | linux app                                                    | ubuntu-latest                               |
| [macos-build.yml](.github/workflows/macos-build.yml)         | macOS app                                                    | macos-latest                                |
| [mobile-builds.yml](.github/workflows/mobile-builds.yml)     | mobile [Android (AAB, APK), iOS (IPA)] apps                  | ubuntu-latest, macos-latest                 |
| [web-build-and-github-pages-deploy.yml](.github/workflows/web-build-and-github-pages-deploy.yml) | static web app and deploys it to GitHub Pages                | ubuntu-latest                               |
| [windows-build.yml](.github/workflows/windows-build.yml)     | windows app                                                  | windows-latest                              |

## 用法

-选择适合您需求的工作流程，即选择对应平台的yml文件。

—复制所选工作流文件的内容。

-在你的存储库 **.github/workflows** 目录下创建一个新的文件并将复制的内容粘贴到其中。

—根据需要修改文件。例如，您可能希望更改触发工作流的事件、工作流的名称、作业的名称等。这取决于你。

-将文件命名为你喜欢的，但要确保它 **.Yml** 扩展名，否则它不会被识别为工作流文件。

-提交更改并将其推送到存储库。

-转到存储库中的Actions选项卡。如果你还没有修改文件，你应该会看到工作流正在运行，这是推送到 **main/master**分支的结果。否则，您可以通过单击“运行工作流”按钮手动触发它。

## 供参考

-根据你特定需求自定义构建命令。Docs:(flet.dev/publish)(https://flet.dev/publish)

-**BUILD_NUMBER** 和 **BUILD_VERSION**用于[版本控制]（https://flet.dev/docs/publish#versioning）。如果您更喜欢在`pyproject.toml `中定义它们。你可以随意将它们从工作流程中删除。

-当构建一个flet应用程序时，只需要安装 **fleet -cli**。要安装的版本由 **FLET_CLI_VERSION** 环境变量指定。

-**PYTHONUTF8** 设置为**1**，确保构建输出以 **UTF-8** 解码。（适用于Windows）

- **FLET_CLI_NO_RICH_OUTPUT** 和 **UV_NO_PROGRESS** (仅在使用uv时有效)设置为 **1**，以减少构建输出的丰富和实时输出。
- 
-您可能会在一些工作流程中发现以下内容：

   - **workflow_dispatch**：用于从Actions选项卡手动触发工作流
     
-在Linux上运行**flutter doctor**时出现以下错误：

' ' '
[✗] Linux toolchain - develop for Linux desktop
    ✗ ninja is required for Linux development.
      It is likely available from your distribution (e.g.: apt install ninja-build), 
      or can be downloaded from https://github.com/ninja-build/ninja/releases
    ✗ GTK 3.0 development libraries are required for Linux development.
      They are likely available from your distribution (e.g.: apt install libgtk-3-dev)
' ' '

一个名为 **Patch for linux build** 的步骤被添加到linux相关的 jobs/workflows 中，通过安装所需的依赖项来解决这个问题。

— 构建命令以详细模式(——verbose)运行，以提供有关构建过程的详细信息。这是非常有用的，当你需要报告一个问题在[Flet repo](https://github.com/flet-dev/flet)。
