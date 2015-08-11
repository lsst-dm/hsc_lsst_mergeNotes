#This is a place to leave notes associated with the hsc merge
#The data entered here will show up at
#http://www.astro.princeton.edu/~nlust/hsc.html
#
#The left and side of the dictionary (the key) may either be the HSC jira
#ticket number as shown below, or the full name of the branch, i.e.
#origin/u/jbosch/fakes.
#
#The right hand column is where you put in any notes as a python string.
#Any valid html markup may be used within the string. For something
#complicated it may be worth defining a string seperately below and adding
#it to the dictionary post initialization.

hscLsstMap = {
              '134':'DM-1944 (Done)',
              '138':'DM-2980, DM-245, DM-2674',
              '145':'DM-2778 (Done)',
              '152':'DM-3157 (Done)',
              '541':'DM-2606 (Done)',
              '551':'Merged in two pieces in DM-240 and DM-3136',
              '669':'Merged in two pieces in DM-3136 and DM-2980',
              '715':'To meas_base on DM-2674.',
              '798':'DM-833',
              '804':'DM-2980',
              '897':'Bulk of the work in DM-833. Partial cherry pick in DM-2980.',
              '972':'DM-2981 (Done)',
              '973':'DM-2981 (Done)',
              '974':'DM-3243 (Done)',
              '975':'DM-833',
              '976':'Missed in DM-2981; rescheduled for DM-3259',
              '1020':'DM-1946 (Done)',
              '1047':'DM-2778 (Done)',
              '1060':'DM-1945 (Done)',
              '1061':'DM-1945 (No-op: abandoned for HSC-1063)',
              '1063':'DM-1945 (Done)',
              '1064':'DM-1945 (Done)',
              '1065':'DM-1945 (Done)',
              '1074':'DM-1386 -> Actually Done on DM-1943 (Done)',
              '1075':'DM-1946[afw] & DM-1945[meas_deblender, pipe_tasks, obs_subaru] (Done)',
              '1083':'DM-1944 (Done)',
              '1109':'DM-1944 (Done)',
              '1112':'Partial cherry pick on DM-2980; the rest probably doesn\'t apply to LSST',
              '1126':'This is a big grab bag of misc fixes. See DM-3264 for sorting out what\'s what. One cherry-pick on DM-2980. All meas_deblender cherry-picks done on DM-1944.',
              '1129':'DM-2606 (Done)',
              '1135':'DM-2606 (Done)',
              '1138':'DM-3258 (Done)',
              '1144':'DM-2913',
              '1153':'DM-2913',
              '1166':'DM-2915',
              '1202':'DM-2915',
              '1203':'DM-2913',
              '1205':'DM-1946 & DM-1945 (Done)',
              '1213':'DM-2778 (Done)',
              '1215':'DM-2606 (Done)',
              '1216':'DM-1954',
              '1217':'DM-2778 (Done)',
              '1218':'DM-1954',
              '1219':'DM-2913',
              '1221':'DM-2778 (Done)',
              '1223':'DM-2913',
              '1228':'DM-2914',
              '1235':'DM-1954',
              '1236':'DM-2913',
              '1237':'DM-2914',
              '1238':'DM-2977',
              '1240':'DM-2977',
              '1243':'DM-Drop',
              '1245':'DM-2914',
              '1246':'DM-Drop',
              '1247':'DM-2976',
              '1249':'DM-2977',
              '1250':'DM-2914',
              '1256':'DM-1954',
              '1260':"DM-2914 (was DM-2975 which is now a Won't Fix)",
              '1264':'DM-2977',
              '1265':'DM-2914',
              '1268':'DM-2914',
              '1270':'DM-2978',
              '1271':'DM-2778',
              '1273':'DM-2977',
              '1274':'DM-2914',
              '1279':'Aperture corrections are handled differently on LSST, but an equivalent fix is in place as of DM-436/b4eb33d',
              '1283':'DM-3139 (Done)',
              }

# Floating commits (just entering as comments for now):
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/1d4ffae208574b210a627a473f3d63a0b09d9825: DM-2778 (Done)
# https://github.com/HyperSuprime-Cam/afw/commit/6fb4676e4b69a29fa8d2cea87d2e22363011408e: DM-2914
#
#coment to test git update
