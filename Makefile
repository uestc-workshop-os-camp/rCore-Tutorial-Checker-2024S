RAND := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')

randomize:
	find user/src/bin -name "*.rs" | xargs sed -i 's/OK/OK$(RAND)/g'
	find check -name "*.py" | xargs sed -i 's/OK/OK$(RAND)/g'

test: randomize
	python3 overwrite.py $(CHAPTER)
	make -C user build BASE=2 TEST=$(CHAPTER) CHAPTER=$(CHAPTER)
	make -C ../os run | tee stdout-ch$(CHAPTER)
	python3 check/ch$(CHAPTER).py < stdout-ch$(CHAPTER)

.PHONY: test randomize
