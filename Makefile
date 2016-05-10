
XMLDUMP=wwwrocksclustersorg.wordpress.2016-05-06.xml

# boiler plate install into new dir, (README exists)
boilerplate:
	jekyll new . --force

# import rocks website xml dump 
run-import:
	ruby -rubygems -e 'require "jekyll-import"; JekyllImport::Importers::WordpressDotCom.run({ "source" => "/Users/nadya/Desktop/$(XMLDUMP)" })'


