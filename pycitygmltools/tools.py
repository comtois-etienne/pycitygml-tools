import subprocess


def exec():
    from . import __executable
    return __executable

def run(command: str, verbose: bool = False):
    """
    Run a command in a subprocess
    """
    out = subprocess.check_output(command, shell=True)
    if verbose: print(out.decode('utf-8'))

def list_to_str(lst: list):
    """
    ['a', 'b', 'c'] -> "a" "b" "c"
    """
    return ' '.join([f'"{x}"' for x in lst])

def help():
    """
    ./citygml-tools --help
    """
    command = f"{exec()} --help"
    run(command, verbose=True)

def version():
    """
    ./citygml-tools --version
    """
    command = f"{exec()} --version"
    run(command, verbose=True)

def stats(citygml_path: str):
    """
    ./citygml-tools stats file.gml
    """
    command = f"{exec()} stats {citygml_path}"
    run(command, verbose=True)

def validate(citygml_path: str, verbose: bool = False):
    """
    ./citygml-tools validate file.gml
    """
    command = f"{exec()} validate {citygml_path}"
    run(command, verbose)

def apply_xslt(citygml_path: str, xslt_path: str, verbose: bool = False):
    """
    ./citygml-tools apply-xslt file.gml stylesheet.xsl
    """
    command = f"{exec()} apply-xslt {citygml_path} {xslt_path}"
    run(command, verbose)

def change_height(citygml_path: str, offset: float, verbose: bool = False):
    """
    ./citygml-tools change-height file.gml 10
    """
    command = f"{exec()} change-height {citygml_path} {offset}"
    run(command, verbose)

def remove_appereance(citygml_path: str, verbose: bool = False):
    """
    ./citygml-tools remove-apps file.gml
    """
    command = f"{exec()} remove-apps {citygml_path}"
    run(command, verbose)

def to_local_appearances(citygml_path: str):
    """
    ./citygml-tools to-local-apps file.gml
    """
    #todo: implement
    print("Not implemented yet")

def clip_textures(citygml_path: str, verbose: bool = False):
    """
    ./citygml-tools clip-textures file.gml
    """
    command = f"{exec()} clip-textures {citygml_path}"
    run(command, verbose)

def subset():
    # todo: implement
    print("Not implemented yet")

def filter_lods(citygml_path: str, lod: str, verbose: bool = False):
    """
    ./citygml-tools filter-lods file.gml 2
    """
    command = f"{exec()} filter-lods {citygml_path} {lod}"
    run(command, verbose)

def reproject(citygml_path: str, epsg: int, verbose: bool = False):
    """
    ./citygml-tools reproject file.gml 4326
    """
    command = f"{exec()} reproject {citygml_path} {epsg}"
    run(command, verbose)

def json_to_gml(cityjson_path: str, verbose: bool = False):
    """
    ./citygml-tools from-cityjson file.city.json
    """
    command = f"{exec()} from-cityjson {cityjson_path}"
    run(command, verbose)

def gml_to_json(citygml_path: str | list, verbose: bool = False):
    """
    ./citygml-tools  to-cityjson file.gml
    """
    if isinstance(citygml_path, list):
        citygml_path = list_to_str(citygml_path)
    command = f"{exec()} to-cityjson {citygml_path}"
    run(command, verbose)

def upgrade_3(citygml_path: str, verbose: bool = False):
    """
    ./citygml-tools upgrade-3 file.gml
    """
    command = f"{exec()} upgrade-3 {citygml_path}"
    run(command, verbose)
