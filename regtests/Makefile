l:
	echo nothing to do

SOURCE_FILES=$(shell cd ../demos; python list_sources.py)
TEST_BASENAMES=$(addprefix test_,$(basename $(SOURCE_FILES)))
PYTHON=python

all:
	$(MAKE) test_demo
	$(PYTHON) run_tests.py
test_demo: 
	rm -f .test*
	$(MAKE) test_golden_files
init_demo:
	rm -rf golden
	mkdir golden
	$(MAKE) create_golden_files

test_golden_files: $(addsuffix .eps,$(TEST_BASENAMES)) \
	$(addsuffix -c.eps,$(TEST_BASENAMES)) \
	$(addsuffix .pdf,$(TEST_BASENAMES)) \
	$(addsuffix -c.pdf,$(TEST_BASENAMES)) \
	$(addsuffix .svg,$(TEST_BASENAMES)) \

create_golden_files:
	for py_file in $(SOURCE_FILES); do \
	    $(MAKE) golden/`basename $$py_file .py`.eps; \
	    $(MAKE) golden/`basename $$py_file .py`.pdf; \
	    $(MAKE) golden/`basename $$py_file .py`-c.eps; \
	    $(MAKE) golden/`basename $$py_file .py`-c.pdf; \
	    $(MAKE) golden/`basename $$py_file .py`.svg; \
	done


run_pychart= cd ../demos; PYTHONPATH=.. PYCHART_OPTIONS="$(1) output=../regtests/$(2) creator=testtest author=testuser creation_date=1/1/2005 title=$*" $(PYTHON) ../regtests/coverage.py -x $(3)

test_%-c.eps:
	$(call run_pychart,color=yes,.test$*-c.eps,$*.py)
	cmp golden/$*-c.eps .test$*-c.eps
test_%-c.pdf:
	$(call run_pychart,color=yes,.test$*-c.pdf,$*.py)
	cmp golden/$*-c.pdf .test$*-c.pdf
test_%.eps:
	$(call run_pychart,,.test$*.eps,$*.py)
	cmp golden/$*.eps .test$*.eps
test_%.pdf:
	$(call run_pychart,,.test$*.pdf,$*.py)
	cmp golden/$*.pdf .test$*.pdf
test_%.svg:
	$(call run_pychart,,.test$*.svg,$*.py)
	cmp golden/$*.svg .test$*.svg

golden/%-c.eps:
	$(call run_pychart,color=yes,$@,$*.py)
golden/%-c.pdf:
	$(call run_pychart,color=yes,$@,$*.py)
golden/%.eps:
	$(call run_pychart,,$@,$*.py)

golden/%.pdf:
	$(call run_pychart,,$@,$*.py)

golden/%.svg:
	$(call run_pychart,,$@,$*.py)

