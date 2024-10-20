import subprocess
import os


def __exec():
    from . import __executable
    return __executable

def __run(command: str, verbose: bool = False) -> str:
    """
    Run a command in a subprocess
    """
    try:
        out = subprocess.check_output(command, shell=True)
        out = out.decode('utf-8')
        if verbose: print(out)
        return out
    except subprocess.CalledProcessError as e:
        print(e.output)

def __list_to_str(lst: list | str) -> str:
    """
    ['a', 'b', 'c'] -> "a" "b" "c"
    """
    if isinstance(lst, list):
        return ' '.join([f'"{x}"' for x in lst])
    return lst

def __get_lines_containing(lines: str, line_content: str) -> None | str | list[str]:
    """
    :param lines: a string containing multiple lines separated by '\n'
    :param line_content: a string to search in each line
    :return: a list of what is after line_content in each line
    """
    lines = lines.split('\n')
    lines = [line for line in lines if line_content in line]
    lines = [line.split(line_content)[1] for line in lines]
    lines = [line.strip() for line in lines]
    lines = [line[:-1] for line in lines]
    lines = None if len(lines) == 0 else lines
    lines = lines[0] if len(lines) == 1 else lines
    return lines

def __get_extension(path: str) -> str:
    """
    Get the extension of a file
    """
    path = path.split('/')[-1]
    return path.split('.')[-1] if '.' in path else None

def __replace_extension(path: str, new_extension: str) -> str:
    """
    Replace the extension of a file
    """
    old_ext = __get_extension(path)
    if old_ext is not None:
        ext_len = len(old_ext) + 1
        path = path[:-ext_len]
    return path + '.' + new_extension

def help() -> str:
    """
    ./citygml-tools --help
    """
    command = f"{__exec()} --help"
    return __run(command, verbose=False)

def version() -> str:
    """
    ./citygml-tools --version
    """
    command = f"{__exec()} --version"
    return __run(command, verbose=False)

def stats(citygml_path: str | list[str], verbose=False) -> None | str | list[str]:
    """
    ./citygml-tools stats file.gml
    :param citygml_path: the path to the citygml file
    :param verbose: print the process output
    :return: the path to the statistics file
    """
    process_str = "Writing statistics as JSON report to file"
    citygml_path = __list_to_str(citygml_path)
    command = f"{__exec()} stats {citygml_path}"
    lines = __run(command, verbose)
    return __get_lines_containing(lines, process_str)

# todo
def validate(citygml_path: str | list[str], verbose: bool = False):
    """
    ./citygml-tools validate file.gml
    """
    pass

# todo
def apply_xslt(citygml_path: str, xslt_path: str, verbose: bool = False):
    """
    ./citygml-tools apply-xslt file.gml stylesheet.xsl
    """
    pass

# todo
def change_height(citygml_path: str, offset: float, verbose: bool = False):
    """
    ./citygml-tools change-height file.gml 10
    """
    pass

def remove_appearances(citygml_path: str | list[str], verbose: bool = False) -> None | str | list[str]:
    """
    ./citygml-tools remove-apps file.gml
    """
    process_str = "Writing output to file"
    citygml_path = __list_to_str(citygml_path)
    command = f"{__exec()} remove-apps {citygml_path}"
    lines = __run(command, verbose)
    return __get_lines_containing(lines, process_str)

# todo
def to_local_appearances(citygml_path: str):
    """
    ./citygml-tools to-local-apps file.gml
    """
    #todo: implement
    pass

def clip_textures(citygml_path: str | list[str], verbose: bool = False) -> None | str | list[str]:
    """
    ./citygml-tools clip-textures file.gml
    """
    process_str = 'Writing output to file'
    citygml_path = __list_to_str(citygml_path)
    command = f"{__exec()} clip-textures {citygml_path}"
    lines = __run(command, verbose)
    return __get_lines_containing(lines, process_str)

# todo
def subset():
    # todo: implement
    pass

# todo
def filter_lods(citygml_path: str, lod: str, verbose: bool = False):
    """
    ./citygml-tools filter-lods file.gml 2
    """
    pass

# todo
def reproject(citygml_path: str | list[str], epsg: int, verbose: bool = False) -> None | str | list[str]:
    """
    ./citygml-tools reproject file.gml 4326
    """
    pass

# todo
def json_to_gml(cityjson_path: str, verbose: bool = False):
    """
    ./citygml-tools from-cityjson file.city.json
    """
    pass

def gml_to_json(citygml_path: str | list[str], verbose: bool = False) -> None | str | list[str]:
    """
    ./citygml-tools  to-cityjson file.gml
    """
    process_str = 'Writing output to file'
    citygml_path = __list_to_str(citygml_path)
    command = f"{__exec()} to-cityjson {citygml_path}"
    lines = __run(command, verbose)
    return __get_lines_containing(lines, process_str)

# todo
def upgrade_3(citygml_path: str, verbose: bool = False):
    """
    ./citygml-tools upgrade-3 file.gml
    """
    pass

def rename(citygml_path: str | list[str], new_name: str | list[str], extension: str | list[str] = None) -> str | list[str]:
    """
    :param citygml_path: the path to the citygml file (extension kept)
    :param new_name: the new name of the file (extension ignored)
    :param extension: the new extension of the file
    :return: the new name of the files
    """
    citygml_path = [citygml_path] if isinstance(citygml_path, str) else citygml_path
    new_name = [new_name] if isinstance(new_name, str) else new_name

    if extension is None:
        extensions = [__get_extension(path) for path in citygml_path]
    elif isinstance(extension, str):
        extensions = [extension] * len(citygml_path)
    else:
        extensions = extension
    extensions = [ext[1:] if ext[0] == '.' else ext for ext in extensions]
    new_names = [__replace_extension(path, ext) for path, ext in zip(new_name, extensions)]

    for old, new in zip(citygml_path, new_names):
        os.rename(old, new)
    
    return new_names

