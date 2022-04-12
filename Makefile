RAND := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')
CHAPTER ?= 

ifeq ($(CHAPTER), 5)
	INITPROC := ch5_usertest
else ifeq ($(CHAPTER), 6)
	INITPROC := ch6_usertest
else ifeq ($(CHAPTER), 7)
	INITPROC := ch7_usertest
endif

LAB = $(shell echo $(CHAPTER)-2 | bc)

randomize:
	find user/src/bin -name "*.rs" | xargs sed -i 's/OK/OK$(RAND)/g'
	find check -name "*.py" | xargs sed -i 's/OK/OK$(RAND)/g'

test: randomize
	python3 overwrite.py $(CHAPTER)
	make -C user build BASE=2 TEST=$(CHAPTER) CHAPTER=$(CHAPTER)
ifdef INITPROC
	cp user/build/elf/$(INITPROC).elf user/build/elf/ch5b_initproc.elf
endif
	make -C ../os run | tee stdout-ch$(CHAPTER)
	python3 check/ch$(CHAPTER).py < stdout-ch$(CHAPTER)

	@for i in $(shell seq $(LAB)); do \
	if ! [ -f ../reports/lab$$i.pdf -o -f ../reports/lab$$i.md ]; then \
		echo "Report for lab$$i needed. Add your report to reports/lab$$i.pdf or reports/lab$$i.md" ; \
		exit 1 ; \
	else \
		echo "Report for lab$$i found." ; \
	fi; \
	done

.PHONY: test randomize
