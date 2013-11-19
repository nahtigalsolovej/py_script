import cubes

# 1. Prepare SQL data in memory
model = cubes.load_model("model.json")
workspace = cubes.create_workspace("sql", model,
                                   url='sqlite:///test.db')

# 2. Create a model
cube = model.cube("datatest")

# 3. Create a browser and get a cell representing the whole cube (all data)
browser = workspace.browser(cube)
cell = cubes.Cell(cube)

# 4. Play with aggregates
result = browser.aggregate(cell)

print "Total\n" \
      "----------------------"

print "Record count: %8d" % result.summary["record_count"]

#
# The End!
#
# ... of the Hello World! example
#
# The following is more than just plain "hello"... uncomment it all to the end.
#
#
# 5. Drill-down through a dimension
#
#

print "\n" \
      "Drill Down by Category (top-level Item hierarchy)\n" \
      "================================================="
# 
result = browser.aggregate(cell, drilldown=["wind"])
# 
for row in result.table_rows("wind"):
    print "%-20s%10d%10d" % ( row.label,
                              row.record["record_count"])

print "\n" \
      "Slice where Category = Equity\n" \
      "================================================="

cut = cubes.browser.PointCut("wind", ["e"])
cell = cubes.browser.Cell(browser.cube, cuts = [cut])

result = browser.aggregate(cell, drilldown=["wind"])

for row in result.table_rows("wind"):
    print "%-20s%10d%10d" % ( row.label,
                              row.record["record_count"])
