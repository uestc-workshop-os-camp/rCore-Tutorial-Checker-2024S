test:
	if [ $(CHAPTER) -ge 4 ]; \
	then cp overwrite/build-elf.rs ../os/build.rs; \
	else cp overwrite/build-bin.rs ../os/build.rs; \
	fi
	if [ $(CHAPTER) -le 2 ]; \
	then cp overwrite/Makefile-ch2 ../os/Makefile; \
	else cp overwrite/Makefile-ch3 ../os/Makefile; \
	fi
	make -C user all CHAPTER=$(CHAPTER)
	make -C ../os run | tee stdout-ch$(CHAPTER)
	expect -f expect/ch$(CHAPTER).exp < stdout-ch$(CHAPTER)

.PHONY: test
