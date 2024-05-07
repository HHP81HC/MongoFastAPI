# MongoDB with FastAPI

```bash
# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
uvicorn app:app --reload
```

{
  // Python environment Path
  "python.languageServer": "Pylance",
  "python.defaultInterpreterPath": "C:\\Users\\%USERNAME%\\.conda\\envs\\etl1\\python.exe",
  //"python.defaultInterpreterPath": "/opt/cloudera/var/user/lur7fe/conda/envs/spark_py36/bin/python3.6",
  /// Linter Rules
  // (we use pylint and SonarLint loacally and pylint and SonarQube in the Pipeline)
  // ! pylint, sonarlint is a VS-Code Package please install it first !
  "python.linting.enabled": true,
  "python.linting.lintOnSave": true,
  "python.linting.pylintEnabled": true,
  "pylint.importStrategy": "fromEnvironment",
  /// Formater
  // (we use black)
  // ! black is a VS-Code Package please install it first !
  "python.formatting.provider": "none",
  "black-formatter.importStrategy": "fromEnvironment",
  "black-formatter.args": [
    "--line-length",
    "120",
    "--skip-magic-trailing-comma",
    "true",
    "--skip-string-normalization",
    "false"
  ],
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.formatOnPaste": false,
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    }
    //"editor.formatOnSaveMode": "modificationsIfAvailable"
  },
  /// Imports
  // ! isort is a VS-Code Package please install it first !
  "isort.importStrategy": "fromEnvironment",
  "isort.check": true,
  /// Python Stuff
  "python.analysis.completeFunctionParens": true,
  /// Docstring
  // ! autoDocstring is a VS-Code Package please install it first !
  // ! --> pres "strg" + "shift" + "2" to generate a documentation
  "autoDocstring.generateDocstringOnEnter": true,
  "autoDocstring.includeName": true,
  "autoDocstring.docstringFormat": "google",
  "autoDocstring.startOnNewLine": true,
  "autoDocstring.guessTypes": true,
  /// Error Lens
  // ! errorLens is a VS-Code Package please install it first !
  "errorLens.delay": 1000,
  "errorLens.enabledDiagnosticLevels": ["error", "warning", "info", "hint"],
  "errorLens.enabled": true,
  "errorLens.excludeBySource": ["sonarlint(ipython:S1192)"],
  "errorLens.enabledInMergeConflict": true,
  "errorLens.enableOnDiffView": true,
  "errorLens.borderRadius": "0px 5em 5em 0px",
  /// Python Testing settings
  // ! pythonTestExplorer is a VS-Code Package please install it first !
  "pythonTestExplorer.testFramework": "unittest",
  "python.testing.unittestEnabled": true,
  "python.testing.unittestArgs": [
    "-v",
    "-s",
    "./tests",
    "-p",
    "*test*.py"
  ],
  "python.testing.pytestEnabled": false,
  "python.testing.autoTestDiscoverOnSaveEnabled": true,
  /// Jupyter settings
  // ! jupyter is a VS-Code Package please install it first !
  "jupyter.interactiveWindow.creationMode": "perFile",
  "jupyter.interactiveWindow.textEditor.autoMoveToNextCell": false,
  "jupyter.askForKernelRestart": false,
  "notebook.outline.showCodeCells": true,
  "notebook.lineNumbers": "on",
  "notebook.output.fontSize": 15,
  "notebook.formatOnSave.enabled": true,
  "notebook.output.textLineLimit": 200,
  "notebook.output.scrolling": true,
  "notebook.compactView": false,
  "notebook.diff.ignoreMetadata": true,
  "notebook.diff.ignoreOutputs": true,
  "notebook.cellToolbarLocation": {
    "default": "right",
    "jupyter-notebook": "left"
  }
}
