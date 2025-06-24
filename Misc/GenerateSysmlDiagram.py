import ast
import os
from pathlib import Path
import webbrowser
from tkinter import filedialog, Tk
from pyvis.network import Network

def choose_main():
    Tk().withdraw()
    return filedialog.askopenfilename(
        title="Select Main Script",
        filetypes=[("Python Files", "*.py")]
    )

def extract_all_imports(filepath):
    tree = ast.parse(Path(filepath).read_text(encoding="utf-8"), filename=filepath)
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
    return imports

def find_local_modules(project_root):
    local_modules = set()
    for path in Path(project_root).rglob("*.py"):
        if "__init__" in path.name:
            continue
        rel = path.relative_to(project_root).with_suffix("")
        dotted = ".".join(rel.parts)
        local_modules.add(dotted)
    return local_modules

def generate_diagram(main_file):
    project_root = Path(main_file).parent.parent  # assume script is 2 levels deep e.g., GuiApp/launcher.py
    main_module = Path(main_file).relative_to(project_root).with_suffix("")
    main_name = ".".join(main_module.parts)

    # Detect internal modules from import paths
    direct_imports = extract_all_imports(main_file)
    all_local = find_local_modules(project_root)
    internal_imports = {imp for imp in direct_imports if any(imp.startswith(m) for m in all_local)}

    # Build diagram
    net = Network(directed=True)
    net.add_node(main_name, label=main_name, color="lightblue", shape="box")

    for mod in internal_imports:
        net.add_node(mod, label=mod, color="lightgray")
        net.add_edge(main_name, mod)

    html_file = project_root / "sysml_diagram.html"
    net.save_graph(str(html_file))
    webbrowser.open_new_tab(str(html_file))
    print(f"✅ Diagram generated at {html_file}")

def main():
    main_file = choose_main()
    if main_file:
        generate_diagram(main_file)
    else:
        print("No file selected. Exiting.")

if __name__ == "__main__":
    main()
