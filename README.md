# python-sample-vs-cpp-extension

This sample is the end product for the walkthrough on https://docs.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio.
You must have the "Python native development tools" option selected for the Python development workload in the Visual Studio 2017 installer.

The superfastcode and superfastcode2 projects contain identical implementations of a hyperbolic tangent function. In the superfastcode project, the
module is exposed to Python using the extension methods for CPython. In the superfastcode2 project, the module is exposed using PyBind11.

The CppAndPython project contains a little Python code that implements the same function using straight Python, then runs all three implementations
to provide comparative results. Note that you may need to update the selected environment under the **Python Environments** node. The sample was
written for Python 3.6 (32-bit). Make sure a suitable environment is selected here.

Because the superfastcode and superfastcode2 C++ projects contain a few hard-coded pathnames and is also configured to compile using the Visual Studio 2017 
toolset, you may need to change a few project properties as described in the table below to make them work on your computer. For the latter two properties,
just set the PYTHONPATH environment variable accordingly, which is the only change needed for Visual Studio 2017.

| Project Property | Value in the example | Notes |
| --- | --- | --- |
| Configuration Properties > General > Configuration Toolset | Visual Studio 2017 (v141) | If using Visual Studio 2015, change to *Visual Studio 2015 (v140)*. In the VS 2015 installer, also make sure that you have the **Programming Languages** > **Visual C++** > **Common Tools for Visual C++ 2015** option selected, which includes the toolset.  |
| C++ > General > Additional Include Directories | %PYTHONPATH%\include | Property must point to the "include" folder of your Python installation. |
| Linker > General > Additional Library Directories | %PYTHONPATH%\libs| Property must point to the "libs" folder of your Python installation. |


# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
