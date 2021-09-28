TARGET := riscv64gc-unknown-none-elf
MODE := release
APP_DIR := src/bin
TARGET_DIR := target/$(TARGET)/$(MODE)
BUILD_DIR := build
OBJDUMP := rust-objdump --arch-name=riscv64
OBJCOPY := rust-objcopy --binary-architecture=riscv64
CP := cp
PY := python3
BUILD_SCRIPTS := build.py
CH_TESTS := 
CHAPTER ?= 

CH2_TESTS := ch2 ch2t
CH3_TESTS_BASE := $(CH2_TESTS) ch3_0
CH4_TESTS := ch4
CH5_TESTS := $(CH4_TESTS) ch5
CH6_TESTS := $(CH5_TESTS) ch6
CH7_TESTS := $(CH6_TESTS) ch7

ifeq ($(CHAPTER), 2)
	CH_TESTS := $(CH2_TESTS)
	BUILD_SCRIPTS := ch2-build.py
else ifeq ($(CHAPTER), 3_0)
	CH_TESTS := $(CH3_TESTS_BASE)
	BUILD_SCRIPTS := ch3-build.py
else ifeq ($(CHAPTER), 3_1)
	CH_TESTS := ch3_1
	BUILD_SCRIPTS := ch3-build.py
else ifeq ($(CHAPTER), 4)
	CH_TESTS := $(CH4_TESTS)
else ifeq ($(CHAPTER), 5)
	CH_TESTS := $(CH5_TESTS)
	INITPROC := ch5_usertest
else ifeq ($(CHAPTER), 6)
	CH_TESTS := $(CH6_TESTS)
	INITPROC := ch6_usertest
else ifeq ($(CHAPTER), 7)
	CH_TESTS := $(CH7_TESTS)
	INITPROC := ch7_usertest
endif

APPS := $(foreach c, $(CH_TESTS), $(wildcard $(APP_DIR)/$(c)*.rs))
ELFS := $(patsubst $(APP_DIR)/%.rs, $(TARGET_DIR)/%, $(APPS))

binary: $(APPS)
	@$(PY) $(BUILD_SCRIPTS) $(CHAPTER)
	@$(foreach elf, $(ELFS), \
		$(OBJCOPY) $(elf) --strip-all -O binary $(patsubst $(TARGET_DIR)/%, $(TARGET_DIR)/%.bin, $(elf)); \
		$(CP) $(elf) $(patsubst $(TARGET_DIR)/%, $(TARGET_DIR)/%.elf, $(elf));)	\

pre:
	@rm -rf $(BUILD_DIR)
	@mkdir -p $(BUILD_DIR)/bin/
	@mkdir -p $(BUILD_DIR)/elf/

env:
	(rustup target list | grep "riscv64gc-unknown-none-elf (installed)") || rustup target add $(TARGET)
	cargo install cargo-binutils --vers ~0.2
	rustup component add rust-src
	rustup component add llvm-tools-preview

all: env binary pre
	@$(foreach t, $(CH_TESTS), $(CP) $(TARGET_DIR)/$(t)_*.bin $(BUILD_DIR)/bin/;)
	@$(foreach t, $(CH_TESTS), $(CP) $(TARGET_DIR)/$(t)_*.elf $(BUILD_DIR)/elf/;)
ifdef INITPROC
	cp $(BUILD_DIR)/elf/$(INITPROC).elf $(BUILD_DIR)/elf/initproc.elf
endif

clean:
	@cargo clean
	@rm -rf $(BUILD_DIR)

.PHONY: elf binary build clean ch2 ch3