
/* Code to register embedded modules for meta path based loading if any. */

#include <Python.h>

/* Use a hex version of our own to compare for versions. We do not care about pre-releases */
#if PY_MICRO_VERSION < 16
#define PYTHON_VERSION (PY_MAJOR_VERSION * 256 + PY_MINOR_VERSION * 16 + PY_MICRO_VERSION)
#else
#define PYTHON_VERSION (PY_MAJOR_VERSION * 256 + PY_MINOR_VERSION * 16 + 15)
#endif

#include "nuitka/constants_blob.h"

#include "nuitka/tracing.h"
#include "nuitka/unfreezing.h"

/* Type bool */
#ifndef __cplusplus
#include "stdbool.h"
#endif

#if 0 > 0
static unsigned char *bytecode_data[0];
#else
static unsigned char **bytecode_data = NULL;
#endif

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
extern PyObject *modulecode_Auxiliary(PyThreadState *tstate, PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_Seeker(PyThreadState *tstate, PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_Shadow(PyThreadState *tstate, PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode___main__(PyThreadState *tstate, PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin32_bootstrap(PyThreadState *tstate, PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin32_system32(PyThreadState *tstate, PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] = {
    {"Auxiliary", modulecode_Auxiliary, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\105\147\157\162\134\111\144\145\141\120\162\157\152\145\143\164\163\134\147\141\155\145\134\163\162\143\134\101\165\170\151\154\151\141\162\171\56\160\171"
#endif
},
    {"Seeker", modulecode_Seeker, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\105\147\157\162\134\111\144\145\141\120\162\157\152\145\143\164\163\134\147\141\155\145\134\163\162\143\134\123\145\145\153\145\162\56\160\171"
#endif
},
    {"Shadow", modulecode_Shadow, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\105\147\157\162\134\111\144\145\141\120\162\157\152\145\143\164\163\134\147\141\155\145\134\163\162\143\134\123\150\141\144\157\167\56\160\171"
#endif
},
    {"__main__", modulecode___main__, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\105\147\157\162\134\111\144\145\141\120\162\157\152\145\143\164\163\134\147\141\155\145\134\163\162\143\134\155\141\151\156\56\160\171"
#endif
},
    {"pywin32_bootstrap", modulecode_pywin32_bootstrap, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\105\147\157\162\134\101\160\160\104\141\164\141\134\114\157\143\141\154\134\120\162\157\147\162\141\155\163\134\120\171\164\150\157\156\134\120\171\164\150\157\156\63\61\61\134\114\151\142\134\163\151\164\145\55\160\141\143\153\141\147\145\163\134\167\151\156\63\62\134\154\151\142\134\160\171\167\151\156\63\62\137\142\157\157\164\163\164\162\141\160\56\160\171"
#endif
},
    {"pywin32_system32", modulecode_pywin32_system32, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, L"\103\72\134\125\163\145\162\163\134\105\147\157\162\134\101\160\160\104\141\164\141\134\114\157\143\141\154\134\120\162\157\147\162\141\155\163\134\120\171\164\150\157\156\134\120\171\164\150\157\156\63\61\61\134\114\151\142\134\163\151\164\145\55\160\141\143\153\141\147\145\163\134\160\171\167\151\156\63\62\137\163\171\163\164\145\155\63\62"
#endif
},
    {NULL, NULL, 0, 0, 0}
};

static void _loadBytesCodesBlob(PyThreadState *tstate) {
    static bool init_done = false;

    if (init_done == false) {
        // Note needed for mere data.
        loadConstantsBlob(tstate, (PyObject **)bytecode_data, ".bytecode");

        init_done = true;
    }
}


void setupMetaPathBasedLoader(PyThreadState *tstate) {
    static bool init_done = false;
    if (init_done == false) {
        _loadBytesCodesBlob(tstate);
        registerMetaPathBasedUnfreezer(meta_path_loader_entries, bytecode_data);

        init_done = true;
    }
}

// This provides the frozen (compiled bytecode) files that are included if
// any.

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    int index;
    int size;
};

static struct frozen_desc _frozen_modules[] = {

    {NULL, 0, 0}
};


void copyFrozenModulesTo(struct _frozen *destination) {
    NUITKA_PRINT_TIMING("copyFrozenModulesTo(): Calling _loadBytesCodesBlob.");
    _loadBytesCodesBlob(NULL);

    NUITKA_PRINT_TIMING("copyFrozenModulesTo(): Updating frozen module table sizes.");

    struct frozen_desc *current = _frozen_modules;

    for (;;) {
        destination->name = (char *)current->name;
        destination->code = bytecode_data[current->index];
        destination->size = current->size;
#if PYTHON_VERSION >= 0x3b0
        destination->is_package = current->size < 0;
        destination->size = Py_ABS(destination->size);
        destination->get_code = NULL;
#endif
        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}

