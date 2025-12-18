/*
 * Pillow internal buffer access shim.
 *
 * This provides fast access to Pillow's internal image buffer.
 * If Pillow's internal headers (Imaging.h) are not available,
 * this provides a stub that returns NULL, causing the Python
 * code to fall back to the slower but safer pixel-by-pixel access.
 */

#include <stddef.h>
#include "pillow.h"

#ifdef HAVE_PILLOW_IMAGING

#include "Imaging.h"

int** get_image32(void* im) {
    ImagingMemoryInstance* image = (ImagingMemoryInstance*) im;
    return image->image32;
}

#else

/* Stub implementation when Pillow internals aren't available */
int** get_image32(void* im) {
    (void)im;  /* unused */
    return NULL;
}

#endif
