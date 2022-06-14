set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'commits_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Commits"
set xtics rotate
set bmargin 6
plot 'commits_by_author.dat' using 1:2 title "Jeremy Weiss" w lines, 'commits_by_author.dat' using 1:3 title "Chris Faxon" w lines, 'commits_by_author.dat' using 1:4 title "Jacob Zamani" w lines, 'commits_by_author.dat' using 1:5 title "DangItJason" w lines, 'commits_by_author.dat' using 1:6 title "gajjas" w lines, 'commits_by_author.dat' using 1:7 title "NA" w lines, 'commits_by_author.dat' using 1:8 title "Jason Nguyen" w lines, 'commits_by_author.dat' using 1:9 title "Nick Arnold" w lines, 'commits_by_author.dat' using 1:10 title "Nicholas Arnold" w lines, 'commits_by_author.dat' using 1:11 title "BuildTools" w lines, 'commits_by_author.dat' using 1:12 title "UnitedBagels" w lines, 'commits_by_author.dat' using 1:13 title "dependabot[bot]" w lines, 'commits_by_author.dat' using 1:14 title "KevTLW" w lines, 'commits_by_author.dat' using 1:15 title "Chris" w lines, 'commits_by_author.dat' using 1:16 title "Adam Cohen" w lines, 'commits_by_author.dat' using 1:17 title "Jason D. Nguyen" w lines, 'commits_by_author.dat' using 1:18 title "Thomas Arturi" w lines, 'commits_by_author.dat' using 1:19 title "dfamilia33" w lines, 'commits_by_author.dat' using 1:20 title "tamckinney" w lines, 'commits_by_author.dat' using 1:21 title "0NotApplicable0" w lines
