RAND := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')

randomize:
	find user/src/bin -name "*.rs" | xargs sed -i 's/OK/OK$(RAND)/g'
	find check -name "*.py" | xargs sed -i 's/OK/OK$(RAND)/g'

test: randomize
	python3 overwrite.py $(CHAPTER)

ifeq ($(CHAPTER), 3)
	make -C user all CHAPTER=3_0
	make -C ../os run | tee stdout-ch3_0
	python3 check/ch3_0.py < stdout-ch3_0
	
	make -C user all CHAPTER=3_2
	make -C ../os run | tee stdout-ch3_2
	python3 check/ch3_2.py < stdout-ch3_2
else
	make -C user all CHAPTER=$(CHAPTER)
	make -C ../os run | tee stdout-ch$(CHAPTER)
	python3 check/ch$(CHAPTER).py < stdout-ch$(CHAPTER)
endif

.PHONY: test randomize
