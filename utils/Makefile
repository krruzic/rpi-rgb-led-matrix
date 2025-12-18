# Utilities directory - currently empty after simplification
# All utility programs have been removed in favor of using external
# graphics libraries like PIL/Pillow for image/video handling.

# Where our library resides.
RGB_LIB_DISTRIBUTION=..
RGB_LIBDIR=$(RGB_LIB_DISTRIBUTION)/lib
RGB_LIBRARY=$(RGB_LIBDIR)/librgbmatrix.a

all:
	@echo "No utilities to build. Use external graphics libraries for image/video handling."

$(RGB_LIBRARY): FORCE
	$(MAKE) -C $(RGB_LIBDIR)

clean:
	@echo "Nothing to clean in utils/"

FORCE:
.PHONY: FORCE
