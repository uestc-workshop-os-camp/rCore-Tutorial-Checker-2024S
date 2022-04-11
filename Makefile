RAND := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')
CHAPTER ?= 
ifeq ($(CHAPTER), 5)
	INITPROC := ch5_usertest
else ifeq ($(CHAPTER), 6)
	INITPROC := ch6_usertest
else ifeq ($(CHAPTER), 7)
	INITPROC := ch7_usertest
endif

randomize:
	find user/src/bin -name "*.rs" | xargs sed -i 's/OK/OK$(RAND)/g'
	find check -name "*.py" | xargs sed -i 's/OK/OK$(RAND)/g'

test: randomize
	python3 overwrite.py $(CHAPTER)
	make -C user build BASE=2 TEST=$(CHAPTER) CHAPTER=$(CHAPTER)
ifdef INITPROC
	cp user/build/elf/$(INITPROC).elf user/build/elf/ch5_initproc.elf
	make -C ../os run | tee stdout-ch$(CHAPTER)
	python3 check/ch$(CHAPTER).py < stdout-ch$(CHAPTER)

.PHONY: test randomize
