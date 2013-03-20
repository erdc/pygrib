import os

def getPaths():
    PREFIX = os.environ['PROTEUS_PREFIX']
    INCDIR = PREFIX+'/'+'include'
    LIBDIR = PREFIX+'/'+'lib'

    # grib_api paths
    grib_api_keys = ['grib_api_dir', 'grib_api_incdir','grib_api_libdir']
    grib_api_dirs = [PREFIX, INCDIR, LIBDIR]
    grib_api_dict = {}
    index = 0
    for key in grib_api_keys:
        grib_api_dict[key] = grib_api_dirs[index]
        index+=1

    # jasper paths
    jasper_keys = ['jasper_dir', 'jasper_incdir', 'jasper_libdir']
    jasper_dirs = [PREFIX, INCDIR, LIBDIR]
    jasper_dict = {}
    index = 0
    for key in jasper_keys:
        jasper_dict[key] = jasper_dirs[index]
        index+=1

    return grib_api_dict, jasper_dict


def generate_setup_cfg(grib_api_dict, jasper_dict):
    """ Initialize input/out for setup.cfg file"""
    f = open('temp.cfg', 'w')

    output = {}
    comments = ['# grib_api directories path',
                '# jasper directories path']
    
    output['directories'] = '[directories]'

    # Directories
    f.write(output['directories']+'\n')
    f.write(comments[0]+'\n')
    for key in grib_api_dict.keys():
        dirVariable = key+'='+grib_api_dict[key]
        f.write(dirVariable+'\n')

    f.write(comments[1]+'\n')
    for key in jasper_dict.keys():
        dirVariable = key+'='+jasper_dict[key]
        f.write(dirVariable+'\n')

    f.close()

if __name__=='__main__':
    """ Script that generates a setup.cfg file which will 
        read system variable PROTEUS_PREFIX and write in
        the necessary include and library directories for
        grib_api and jasper. """
    
    [grib_api_dict, jasper_dict] = getPaths()

    generate_setup_cfg(grib_api_dict, jasper_dict)
