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
              '189':'DM-3957',
              '152':'DM-3157 (Done)',
              '541':'DM-2606 (Done)',
              '551':'Merged in two pieces in DM-240 and DM-3136',
              '669':'Merged in two pieces in DM-3136 and DM-2980',
              '670':'DM-245 (Done)',
              '715':'To meas_base on DM-2674.',
              '756':'DM-3677 (Done)',
              '798':'DM-833 (Done)',
              '804':'DM-2980 (Done)',
              '897':'Bulk of the work in DM-833. Partial cherry pick in DM-2980.',
              '972':'DM-2981 (Done)',
              '973':'DM-2981 (Done)',
              '974':'DM-3243 (Done)',
              '975':'DM-833 (Done)',
              '976':'Missed in DM-2981; rescheduled for DM-3259',
              '987':'DM-3942 [obs_subaru] (Done) Still need [daf_butlerUtils, ip_isr, hscPipe(?)] changesets',
              '1004':'DM-2914 [meas_deblender, afw] (Done)',
              '1020':'DM-1946 (Done)',
              '1047':'DM-2778 (Done)',
              '1060':'DM-1945 (Done)',
              '1061':'DM-1945 (No-op: abandoned for HSC-1063)',
              '1063':'DM-1945 (Done)',
              '1064':'DM-1945 (Done)',
              '1065':'DM-1945 (Done)',
              '1074':'DM-1386 -> Actually Done on DM-1943 (Done)',
              '1072':'DM-3811 (Done)',
              '1075':'DM-1946[afw] & DM-1945[meas_deblender, pipe_tasks, obs_subaru] (Done)',
              '1083':'DM-1944 (Done)',
              '1085':'DM-3693 (Done)',
              '1086':'DM-3693 (Done)',
              '1106':'DM-3911 Omitting eups versioning changes (Done)',
              '1109':'DM-1944 (Done)',
              '1112':'Partial cherry pick on DM-2980; the rest probably doesn\'t apply to LSST',
              '1116':'DM-2914 [meas_deblender] (Done)',
              '1126':'This is a big grab bag of misc fixes. See DM-3264 for sorting out what\'s what. One cherry-pick on DM-2980. All meas_deblender cherry-picks done on DM-1944.',
              '1129':'DM-2606 (Done)',
              '1135':'DM-2606 (Done)',
              '1138':'DM-3258 (Done)',
              '1144':'DM-2913',
              '1147':'DM-2914 [meas_deblender] (Done)',
              '1153':'DM-2913',
              '1160':'Compiler warning fix duplicates DM-4101, which is already fixed on LSST.',
              '1166':'DM-2915 (Done)',
              '1175':'DM-3811 (Done)',
              '1196':'DM-4323',
              '1202':'DM-2915 (Done)',
              '1203':'DM-2913',
              '1205':'DM-1946 & DM-1945 (Done)',
              '1213':'DM-2778 (Done)',
              '1215':'DM-2606 (Done)',
              '1216':'DM-1954 (Done)',
              '1217':'DM-2778 (Done)',
              '1218':'DM-1954 (Done)',
              '1219':'DM-2913',
              '1221':'DM-2778 (Done)',
              '1223':'DM-2913',
              '1228':'DM-2914 (Done)',
              '1235':'DM-1954 (Done)',
              '1236':'DM-2913',
              '1237':'DM-2914 (Done)',
              '1238':'DM-2977 (Done)',
              '1240':'DM-2977 (Done)',
              '1243':'DM-Drop',
              '1245':'DM-2914 (Done)',
              '1246':'DM-Drop',
              '1247':'DM-2976',
              '1249':'DM-2977 (Done)',
              '1250':'DM-2914 (Done)',
              '1256':'DM-1954 (Done)',
              '1259':'DM-4235',
              '1260':"DM-2914 (Done) (was DM-2975 which is now a Won't Fix)",
              '1264':'DM-2977 (Done)',
              '1265':'DM-2914 (Done)',
              '1268':'DM-2914 (Done)',
              '1270':'DM-2978',
              '1271':'DM-2778 (Done)',
              '1273':'DM-2977 (Done)',
              '1274':'DM-2914 (Done)',
              '1275':'DM-3911 (Done)',
              '1276':'DM-4235',
              '1279':'Aperture corrections are handled differently on LSST, but an equivalent fix is in place as of DM-436/b4eb33d',
              '1283':'DM-3139 (Done)',
              '1285':'DM-3911 Omitting eups versioning changes (Done)',
              '1292':'DM-3911 Omitting eups versioning changes (Done)',
              '1321':'DM-3911 (Done)',
              }

# Floating commits (just entering as comments for now):
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/1d4ffae208574b210a627a473f3d63a0b09d9825: DM-2778 (Done)
# https://github.com/HyperSuprime-Cam/afw/commit/6fb4676e4b69a29fa8d2cea87d2e22363011408e: DM-2914 (Done)
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/071fcadc016908a10583c746f0a8e79df2a45ead: DM-3678 (Done)
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/e73c5e447ac0b8a71926d3e78fec30aad4beee91: DM-3678 (Done)
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/15bb812578531766199e9a1ee41cc707fb3d9873: DM-3678 (Done)
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/44f75bc60b41c5f77b323a8d9981048ef7e5f3c4: DM-3678 (Done)
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/4413db4610e4793727e591f395f5ad8cd0cb6030: DM-3678 (Done)
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/67efacaccf8346fdfa1b450617aebabddb2b7ec0: DM-3678 (Done)
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/b1bc91ed1538607eb90e070881a82498fd551909: DM-3678 (Done)
# https://github.com/HyperSuprime-Cam/meas_algorithms/commit/6b36f4d757187d30142a7e026754a07ffeb8dea2: DM-3678 (Done)
# https://github.com/HyperSuprime-Cam/pipe_tasks/commit/e9db5c0dcdca20e8f7ba71f24f8b797e71699352: DM-3693 (Done)
# https://github.com/HyperSuprime-Cam/pipe_tasks/commit/c2d89396923f9d589822c043ed8753647e70f3f6: DM-3693 (Done)
# https://github.com/HyperSuprime-Cam/pipe_tasks/commit/cf5724b852937cfcef1b71b7a372552011fda670: DM-3693 (Done)
# https://github.com/HyperSuprime-Cam/pipe_tasks/commit/ab6cb9e206d0456dc764c5ef78ac80ece937c610: DM-3693 (Done)
# https://github.com/HyperSuprime-Cam/pipe_tasks/commit/08a8ec029dd52ac55e47b707a6905df061a40506: DM-3693 (Done)
# https://github.com/HyperSuprime-Cam/pipe_tasks/commit/9e8563fd8d630dad967786387b1f27b6bc7ee039: DM-3693 (Done)
# https://github.com/HyperSuprime-Cam/obs_subaru/commit/52733a7ab1731a15cbb93151851f57cec276f928: DM-3693 (Done)
# https://github.com/HyperSuprime-Cam/obs_subaru/commit/bae672c0e42857d0d1beeb532af3eb6934ac3cea: DM-4022 (Done)
# https://github.com/HyperSuprime-Cam/daf_persistence/commit/6bf2ae5b3ad015494f8a095d1d7a51e8a8ce150e: DM-3911 (Done)
# https://github.com/HyperSuprime-Cam/obs_subaru/commit/f908cffcbc61b2f842b30c4821ee29ea2160538d: DM-2793 (Done)
#
#coment to test git update
