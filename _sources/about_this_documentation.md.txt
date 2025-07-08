# 𓂀 About this Sphinx documentation

Sphinx is a powerful tool for generating technical documentation in multiple formats (such as HTML, PDF, EPUB, among others) from source files written in reStructuredText (.rst).  
It is widely used in Python projects due to its integration with docstrings and its compatibility with tools like ReadTheDocs or GitHub Pages.

By using Sphinx, you can keep your documentation synchronized with the source code, ensuring it's always up-to-date and professionally presented.

## 📄 How to generate/update the documentation?

```{warning}
⚠️ IMPORTANT: All commands must be executed from your project's docs/ folder. To enter it, use:
```

```bash
cd docs
```

1. Automatically generate .rst files
Sphinx can scan your source code and generate the .rst files that will serve as the foundation for your documentation:

```bash
sphinx-apidoc -o source ../src
```

-   -o source: indicates that the generated .rst files will be saved in the source/ folder
-   ../src: is the path to the source code you want to document (adjust this if you use a different folder name)

💡 Note: This will overwrite previously generated .rst files, so make a backup if you've manually modified them.

2. Compile the documentation in HTML format

After generating the .rst files, compile your documentation with:

```bash
make html
```

This creates a build/html/ folder containing the navigable documentation. Open build/html/index.html in your browser to view it locally.

3. (Recommended) Clean previously generated files
Before recompiling, clean previous files with:

```bash
make clean
```

```{warning}
⚠️ (Use with caution) This deletes the contents of the build/ folder to prevent inconsistencies in the next compilation.
```
