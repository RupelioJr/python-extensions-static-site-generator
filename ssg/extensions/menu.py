from ssg import hooks, parsers

files = []

def collect_files(source, site_parsers):
    hooks.register("collect_files")
    valid = lambda(p, isinstance(p, parsers.ResourceParser))