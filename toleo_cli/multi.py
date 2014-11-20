import multiprocessing
import toleo


def worker(item):
    name, data = item
    src = data.get('src')
    pkg = data.get('pkg')

    src_name = src.pop('name', name)
    src_type = src.pop('type', 'generic')
    if src_type == 'generic':
        software = toleo.GenericSoftware(src_name, **src)
    elif src_type == 'pypi':
        software = toleo.PypiSoftware(src_name, **src)
    elif src_type == 'github':
        software = toleo.GithubSoftware(src_name, **src)
    elif src_type == 'bitbucket':
        software = toleo.BitbucketSoftware(src_name, **src)

    pkg_name = pkg.pop('name', name)
    pkg_type = pkg.pop('type')
    if pkg_type == 'aur':
        package = toleo.AurPackage(pkg_name, **pkg)

    return (software, package)


def handle(config):
    pool = multiprocessing.Pool()
    results = pool.map(worker, config.items())
    pool.close()
    pool.join()
    return results
