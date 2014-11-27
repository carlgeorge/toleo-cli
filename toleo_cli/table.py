import prettytable


class SoftwareTable(prettytable.PrettyTable):
    def add_software_row(self, src, pkg):
        if src.version > pkg.version:
            status = 'UPDATE'
        else:
            status = 'OK'
        self.add_row([pkg.name,
                      src.name,
                      pkg.version.evr,
                      src.version.version,
                      status])


def create_table(results):
    table = SoftwareTable(['PACKAGE', 'PROJECT', 'REPO', 'SOURCE', 'STATUS'])
    for result in results:
        software, package = result
        table.add_software_row(software, package)
    return table
