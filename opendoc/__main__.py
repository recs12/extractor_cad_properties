# By Slimane .R
# Snippet of code to extract JDELITM number from 
# all parts in a specific folder.
# I haven't been able to extract without opening Solidedge
# You need to open a session in solidedge to use this code.

import clr

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

from SolidEdgeFileProperties import Properties

import os
from api import Api



def extract_properties_folder(location_parts):
    try:
        session = Api()
        fasteners_folder = os.listdir(location_parts)
        name_of_folder = os.path.basename(location_parts)
        for par in fasteners_folder:
            if par.endswith('.par') or par.endswith('.PAR'):
                with open(os.path.join(location_parts, name_of_folder+'.py') , 'a+') as inv:
                    # item = session.active_document()
                    item = session.open_document(os.path.join(location_parts, par))
                    properties = item.Properties
                    cad_name = str(par)
                    jde_number= properties('Custom').Item('JDELITM').value
                    print("%s : %s," %(cad_name, jde_number))
                    inv.write("\"{0}\": {1},\n".format(cad_name, jde_number))
                    session.close_document()

    except AssertionError as err:
        print(err.args)
    else:
        pass

def main():
    extract_properties_folder(r'C:\Users\Slimane\Desktop\solidedge\Hardware\Nuts')

if __name__ == "__main__":
    main()
