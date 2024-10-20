import os
import stat

from .tools import (
    help,
    version,
    stats,
    validate,
    apply_xslt,
    change_height,
    remove_appearances,
    to_local_appearances,
    clip_textures,
    subset,
    filter_lods,
    reproject,
    json_to_gml,
    gml_to_json,
    upgrade_3, 
    rename,
)


__release = '2.3.2'
__latest = f'https://github.com/citygml4j/citygml-tools/releases/download/v{__release}/citygml-tools-{__release}.zip'
__executable = os.path.expanduser(f"~/.citygml-tools/citygml-tools-{__release}/citygml-tools")


if not os.path.exists(os.path.expanduser("~/.citygml-tools")):
    os.makedirs(os.path.expanduser("~/.citygml-tools"))

if not os.path.exists(os.path.expanduser(f"~/.citygml-tools/citygml-tools-{__release}.zip")):
    import urllib.request
    urllib.request.urlretrieve(__latest, os.path.expanduser(f"~/.citygml-tools/citygml-tools-{__release}.zip"))

if not os.path.exists(os.path.expanduser(f"~/.citygml-tools/citygml-tools-{__release}")):
    import zipfile
    with zipfile.ZipFile(os.path.expanduser(f"~/.citygml-tools/citygml-tools-{__release}.zip"), 'r') as zip_ref:
        zip_ref.extractall(os.path.expanduser("~/.citygml-tools"))

os.chmod(__executable, os.stat(__executable).st_mode | stat.S_IEXEC)


__all__ = [
    "help", 
    "version",
    "stats",
    "validate",
    "apply_xslt",
    "change_height",
    "remove_appearances",
    "to_local_appearances",
    "clip_textures",
    "subset",
    "filter_lods",
    "reproject",
    "json_to_gml",
    "gml_to_json",
    "upgrade_3",
    "rename",
]
