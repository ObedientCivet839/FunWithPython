### PROBLEM STATEMENT
# https://leetcode.com/problems/jump-game/

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


# Method 1:
# 
# Idea:
# - Create a step array.
# - The idea is each step needs to be covered in order from start to finish.
# - At each index, set all the values next to True.
# - Optimized: Go from the back and shortcut if the rest is already set to True
#
# Runtime: O(???)
# 
#
class Solution1:
    def canJump(self, nums: list[int]) -> bool:
        N = len(nums)
        steps = [False] * N
        steps[0] = True # set the first step to True always
        for i in range(N):
            # BUG 1: Start from the end
            for j in range(min(i + nums[i], N - 1), i, -1):
                if steps[j]: # already set the rest to True
                    break
                steps[j] = True
        res = True
        for i in steps:
            if not i:
                return False
        return True

# Method 2: (Solution)
# 
# Idea:
# - Traverse from the back of the list.
# - If an index can reach the goal (i + nums[i] > goal), move the goal to the index
#
# Runtime: O(N)
# 
#
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        N = len(nums)
        goal = N - 1
        for i in range(N - 2, -1, -1): # traverse from the back of the list
            if i + nums[i] >= goal: # can reach the goal
                goal = i
        return goal == 0


### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            nums: list[int]
            expected: int

        testcases = [
            TestCase(
                name="1",
                nums = [2,3,1,1,4],
                expected = True
            ),
            TestCase(
                name="2",
                nums = [3,2,1,0,4],
                expected = False
            ),
            TestCase(
                name="3",
                nums = [11990,13129,14867,2620,8283,13879,11543,18909,736,9132,15278,11048,7370,4204,1264,11244,15042,17391,1520,11387,7441,19806,16892,14590,18432,11875,5952,5547,6411,10989,11267,12025,12192,2921,15434,5033,3669,3972,19906,14631,18191,16297,9378,17404,16035,8873,12065,12133,12041,17878,9720,11604,10285,11255,9553,19381,8399,7925,431,4979,333,16650,2204,4353,5491,13413,11745,4143,8140,10690,11315,13099,7232,2096,11856,10345,18509,11767,10603,12974,2094,9518,6827,5332,4922,10143,14751,16605,7597,15625,1726,15709,8036,17214,18966,9709,8038,19259,12978,5689,18418,18935,17233,16693,15477,14595,14895,11837,7208,8657,10237,7935,13064,3542,70,2538,16560,9610,4685,7078,17838,15200,7753,7661,11214,13265,14649,7146,15499,5394,7668,10556,3583,9231,13448,18954,4878,7868,4937,15742,16768,16205,7142,2534,11290,11503,16782,19813,5462,10319,14704,10420,19142,10375,14905,19908,16277,9084,10174,685,18854,12590,8656,4343,9957,15754,7524,3254,8136,2664,18597,3875,17062,3840,10495,15808,14765,18050,11407,129,8983,13238,6681,16262,4479,18952,18378,1134,7723,12594,1676,1497,1765,6342,6786,9334,7479,11260,16805,2842,6352,5485,12494,4121,9347,3924,8604,3264,19390,13004,7730,12657,18055,5136,11358,687,15405,10460,3241,5425,4060,2613,4627,4246,3606,15395,3026,12845,16280,8261,15907,19189,6983,17783,9208,11644,14746,8743,2127,16576,7026,14509,11337,10283,8838,3634,16959,16080,16848,6888,15944,8473,4307,4736,10333,1132,10204,9935,19432,5500,18713,9807,6872,2610,5498,4911,15735,18065,3742,10509,9227,5578,893,12511,18696,11056,11687,9876,4099,5427,16393,12769,10208,8357,9674,11269,16848,14470,11055,7991,7243,19899,10026,12455,14998,18918,6370,13169,133,8253,11783,3310,15519,17468,19215,1261,19575,15634,8683,4771,10337,6409,5679,8007,8010,18261,8917,9565,7206,4724,16172,542,1137,9488,9605,14722,4108,15032,19473,7288,18863,5647,19067,14161,7367,8707,12359,14778,5739,7979,16296,12959,4614,14765,4053,11676,13145,19472,13602,10726,14190,2846,3400,15218,7384,11387,15084,180,772,18855,9572,9693,15339,11835,19464,13120,3623,364,11389,4903,9927,5931,17532,18881,19697,8423,4335,6384,10935,12034,12850,10943,13470,6525,7188,11306,13789,7931,16904,3187,4642,1298,15409,13115,3233,11664,8236,5104,9854,5985,999,17654,10034,17418,7348,9783,5362,11541,6481,9524,8552,18217,19835,17468,9682,6224,8477,11166,3695,14483,735,11281,2792,7804,2522,9316,6709,19503,17540,7233,15166,18287,11750,11750,17539,17202,11719,3903,14717,17514,9256,16258,19728,11290,18705,11754,10581,8456,14791,1973,5293,9667,5807,322,16440,15702,19686,17167,7752,12279,15672,19390,2343,10822,4677,12084,17804,16205,19950,11342,16353,627,15061,18051,14605,12905,17118,15708,11946,6816,731,14543,7138,5718,8237,7602,16644,5708,5706,13292,8459,12139,16659,5757,14622,8936,19086,97,15326,14952,1820,11352,4578,14520,15945,5494,6546,5,16466,1133,5296,2930,3366,619,5055,2157,11215,1514,18693,14783,14843,9829,17275,12848,16632,13145,10253,1160,14132,2127,10452,4949,14314,12602,14142,1632,18874,17177,6580,7402,19485,17763,9581,180,1308,11128,4831,588,10474,6945,11611,9461,5214,10861,10150,17070,9125,3290,17414,4291,11357,8805,1626,4917,8970,6464,12698,11,2719,19088,8205,10072,1412,1427,43,12758,17489,2828,11054,3472,2528,4264,5302,18132,14870,2782,9748,13169,10212,19096,14035,889,9137,9816,9694,8214,18982,8767,1291,9814,6399,16623,4436,4395,1332,1239,3491,15302,19937,18810,18736,9929,13120,19901,3906,16133,18372,2067,18197,12420,19653,11591,5948,14616,14834,13220,4311,13592,18318,5256,5754,8917,19717,9126,637,8001,1697,3523,8251,17999,9070,6546,17515,13743,91,16383,2710,3123,16877,7075,7173,10487,8797,13326,13636,5009,6480,13791,9184,18177,4808,4564,18874,12549,2677,11354,17981,11532,12661,19024,18355,2462,15756,627,18220,5058,10760,8614,19557,8955,10050,18543,8881,19785,9982,7512,11334,16757,10114,4489,10051,7846,1133,6322,18887,3819,9469,2096,12763,17451,7028,8692,9026,14717,15600,13129,756,14558,15104,4809,19951,4070,18659,3808,1683,8410,7672,14810,19801,1613,3999,17890,4312,13163,2067,6252,5535,12656,6426,1060,8315,238,4292,5239,19238,16975,3448,17519,4202,5110,9993,15460,11219,11818,12177,16002,19655,8420,638,17168,13422,2025,8787,16968,12263,1611,129,18720,7404,12094,19274,9480,16838,16508,17059,13172,13952,11410,4827,3194,7365,18255,7308,12131,16755,6783,17089,1356,2861,3372,17709,7862,13210,2545,13503,6441,2626,532,11390,11983,7112,7047,18820,1678,9716,7466,5305,18551,12258,4270,14133,14784,1712,13593,10797,11195,9423,4853,19003,19429,16922,13238,7049,10136,4066,18984,13543,12847,567,268,11309,9199,6752,9117,1940,17911,19054,17425,5876,2523,13695,7207,10302,3453,3006,13655,16399,3880,17281,5204,2940,15303,12663,1592,6824,16196,4112,15251,4992,10721,16866,2871,803,17443,17245,2149,4728,1954,14995,12608,16747,7441,3661,7435,15141,9384,6962,8073,15423,7673,1979,5827,9805,229,4326,19154,19258,11299,17641,17100,6074,14835,17589,1932,2658,9867,14606,14480,5858,7150,7771,13284,3063,4884,2994,7133,19120,19268,5115,15842,1769,15610,2773,13022,6332,10939,9279,9874,3642,11067,19885,5180,15428,4941,11786,15277,15079,4631,18374,9796,87,7966,19318,15010,8669,11403,10749,723,17123,19629,12739,2046,9790,11266,7941,4965,4306,2512,15986,1592,743,8657,19509,8309,18836,626,12023,15195,13033,4370,9761,15654,1203,5654,7560,8261,18209,16207,2798,6964,13096,11427,17224,5190,15796,16204,15054,9628,13498,1656,16435,632,16824,16476,11749,3698,12709,8977,3470,10954,12022,3231,17244,7184,16679,8097,18756,13064,13351,7884,14303,5682,15584,1780,18301,14144,4972,6204,13131,11650,11582,13880,10734,11561,13947,17927,16070,18815,18734,10124,2226,15313,17433,11787,11986,13179,16648,6979,17655,19152,8477,3572,16315,2782,651,15937,7505,9268,4869,14590,6457,6031,9630,3780,16124,8009,19068,3738,6236,8336,14708,1323,13551,11225,12794,14526,16532,16317,10736,4060,13964,5611,13939,5807,2560,7249,16896,6393,2530,12391,15172,17584,1744,7332,17118,8482,13942,9039,15983,12415,15841,7389,19160,19640,14230,5127,12340,19231,16470,18702,11664,7151,18341,19025,928,753,18806,6620,4317,3632,11587,2770,18003,16490,8489,15884,5621,18606,10724,2176,14386,13948,1394,3085,10013,18415,2912,12824,14666,5986,8573,10001,12815,7571,13108,3696,16099,12401,6459,11585,12324,13264,17329,7599,7309,17600,2677,12533,18168,17760,18292,9801,15819,394,1902,767,15302,19408,14022,9810,668,10061,16611,16847,4341,19753,9798,471,2407,12794,5220,18932,14742,10213,2331,4963,3742,16460,5217,5897,8980,3100,15837,14261,6326,5865,1121,1378,3589,11218,17848,17505,18118,5552,6210,3211,19852,10611,19238,4486,11922,13431,3472,17899,12351,18483,728,5357,3780,8491,18722,10213,557,7362,7174,12620,5655,9860,6444,16658,158,18502,8640,14009,3647,18071,15747,8860,5227,6658,14051,16046,10284,17581,7733,10941,19187,18273,17424,3113,13016,18115,4492,13703,13417,14933,19626,7382,3933,2048,1987,10975,14845,16331,5420,14495,16490,2955,18473,306,18600,7540,8451,19298,19912,15654,8762,17678,10100,10631,12771,7403,15700,14437,14118,9195,1715,1475,14251,1277,13430,3028,9601,15499,5848,9139,1676,17536,12715,2267,17966,692,1924,12760,2111,3408,18054,18596,5640,15443,17962,17698,4934,12657,13270,103,9,2880,7558,14764,19557,11931,12670,8534,8562,46,9059,14806,6038,9918,89,2580,9359,10116,16377,8865,10690,9900,16328,14779,13323,10968,241,12286,3159,5634,11958,7868,7932,15744,14162,17164,6823,13960,686,2991,13823,16815,11140,1064,14352,13136,15004,5758,9404,2191,4269,19272,13001,8229,6425,15567,13715,17918,9645,12356,5045,5162,11623,6283,10698,4423,3257,12566,3134,10072,1402,8908,18817,12308,17338,16266,14825,7525,11703,19152,18859,3718,3050,12289,9163,7112,19199,14901,5581,4824,13739,19958,8834,4683,2351,5855,5670,6344,1676,2043,3218,10103,18465,11971,2900,9780,12803,16336,3605,18329,3540,18737,12574,7154,7961,14922,13455,15639,14957,17961,5795,9171,1859,11038,12897,2563,3265,10174,7315,932,8214,8111,11977,19642,8185,17829,11720,10428,15727,16690,15619,1321,9407,9974,9637,4669,1805,4711,11831,9207,8517,18956,14056,14991,1953,3824,17714,280,9770,11228,11647,15358,10579,14398,13248,15719,2824,15956,7890,18915,12525,3944,11175,16625,8082,2903,12176,7217,13515,16375,16309,10661,8667,1227,16269,19507,4748,14164,11919,5826,4703,14051,16594,16053,18114,6897,11004,14931,7955,7781,19260,1340,13531,12760,18314,16187,5403,3577,3109,19847,17673,13768,13259,7420,15289,16393,4981,4112,5572,4136,6106,3231,5560,11590,3681,16271,1533,2460,17599,2153,5440,13302,11630,7440,14120,8267,16994,4861,16441,13400,15212,17896,9834,8763,14501,2236,11181,1271,10786,13245,7033,13596,3905,3669,18520,6347,3622,10517,8442,16262,6290,13211,18421,17079,1422,1643,6948,13858,12743,8905,243,11087,7085,17476,12171,5941,8469,16748,2319,16842,3239,12753,7781,14006,17348,9359,1862,7184,14609,14157,16520,10858,8109,8789,11213,1056,4533,16339,6128,18536,10213,8324,14557,17455,10405,2177,6559,17184,7289,9124,17586,6980,2111,1050,5964,534,19612,14173,16448,6093,5290,659,835,16050,10768,16615,19027,15040,923,9691,15229,19709,9674,9270,19504,19854,11296,748,540,1059,9196,485,14454,12841,7192,14354,7288,4430,16286,18530,16191,7662,18305,15615,6492,10571,4122,3756,14509,14254,11471,12044,2616,11282,3569,11161,11019,16278,12189,17154,2742,15103,3598,13476,9561,17589,14306,8982,18498,19787,11607,1409,11831,2049,5335,15562,6959,10205,8318,4542,15020,8601,13238,11591,1534,18540,9789,9576,9443,1132,13706,15470,12854,5478,1051,355,16714,406,15062,19964,8878,7857,15926,118,14150,6341,16032,17704,9521,6554,4869,4538,9416,7938,1135,13483,4524,13976,3270,19609,3556,19124,1053,827,18746,497,13109,7321,7508,3472,364,17232,19639,1970,6906,15338,10431,8258,848,9144,2721,9167,14368,6537,5333,8427,11711,14140,12204,11962,15105,11127,8361,8351,14974,373,12550,13578,10706,4745,19434,3913,6754,4511,1600,3458,1806,11075,10213,18313,12575,14897,8678,7527,9629,16730,18848,6961,7151,2161,19498,14917,2858,16932,6956,6381,5551,17921,5196,12208,17359,8928,4764,3599,8358,16918,14943,6541,2883,19186,15389,3503,9039,16358,5473,15033,1613,17229,9184,11712,2732,1439,1685,11310,12339,5242,4978,18836,17530,19849,8009,13672,6583,11843,12562,1334,17192,18764,9180,14281,14022,2051,17256,10534,703,3726,14579,4021,16698,2572,9265,658,19446,6759,6654,783,18401,13190,9780,15076,5285,7044,5882,4553,2675,12780,7125,6361,9621,8103,12485,4718,11455,12679,4775,247,17976,19678,7382,1544,12413,6085,12271,5494,10170,7384,109,417,14220,18784,17955,17448,5648,2556,19873,1460,17339,2619,8137,6461,16367,9047,7800,7643,14575,8017,8655,11447,12379,5523,4461,4532,8160,14961,12825,17344,11144,7086,12704,8667,5177,3357,110,7651,18489,4098,7664,38,11943,13257,11053,9492,16592,9038,14032,16272,7177,5489,2925,1285,6885,15197,5695,15489,19159,5253,15341,4894,12636,3991,3972,13601,11549,19709,10634,14334,17899,10597,18337,15817,1783,8640,11777,12027,16139,3907,18902,2371,4906,16331,5815,16998,18747,18166,13720,4876,1016,9897,12201,10224,1782,16155,6130,4290,9392,10304,15127,5617,18156,2721,15342,6877,17962,11967,12404,8574,1336,6115,13949,978,16756,17263,18722,15753,6941,9608,12451,8156,1886,11761,13765,10368,10156,16598,542,19756,3119,1196,14528,600,11808,10358,14467,7602,17733,10945,7864,16366,5746,15311,12005,12061,13770,3229,9434,4923,4771,15004,5556,4361,19812,72,11992,14372,7017,6853,938,1486,15121,18015,11146,13245,19773,16271,19179,18970,11563,12907,11666,1689,10414,8413,8442,12468,7830,13672,4978,8233,12013,7050,938,14075,16914,16145,16751,609,19152,4880,722,5144,14484,1771,8977,17737,18218,18426,9111,14402,2540,9577,13764,972,1268,19161,6809,2474,2287,8666,1310,4918,9756,15708,1057,7525,12030,10749,108,9543,11958,17320,4640,17435,487,4322,15359,6789,13101,4386,15694,7510,1213,9386,15157,16027,5357,10666,7825,491,15513,4876,18942,12710,4217,17071,2203,1021,4179,18399,13565,19192,14847,2184,9426,4584,19820,3797,15905,11772,3696,17224,13690,17815,16147,6606,13112,14523,2379,15921,6239,699,665,18414,2219,12395,16667,9411,7604,2551,19316,17897,10291,1610,3358,7241,3833,15833,4639,14564,12378,13965,6084,8770,16978,18618,902,5264,2227,19848,16341,3836,8114,13807,7137,6083,6721,6664,16430,19645,4690,18882,1424,2039,18396,8256,8165,14345,13396,9294,17262,10323,9226,19838,18321,15704,2005,10949,18146,11305,13064,13574,2948,6127,14546,4905,4909,15281,5809,10532,3023,19186,18544,12517,17094,19052,13375,4133,19547,14107,8407,4453,15223,10926,2316,8385,10056,14294,5692,6008,16065,434,11067,17889,9127,10418,15859,12398,4244,10072,14533,2125,4190,19484,3366,9511,5670,11920,18180,14461,6286,7256,9971,7344,2801,4514,1131,14704,12964,18525,17044,895,17387,6268,1668,2874,3726,13058,4288,17942,18325,14972,14442,7511,1371,5279,1404,3726,11401,14589,15293,62,9502,11969,12763,4853,15234,3082,9760,12405,13056,16104,9649,17085,8402,17258,2810,19036,16389,6474,2571,13821,12164,14857,18890,17969,15161,6319,13043,4169,1253,3126,6095,13232,12148,3482,6326,2180,11216,5404,18652,7487,3049,13234,16858,17110,16543,12441,19224,62,14866,10399,5396,10473,8236,13899,3479,16049,7135,15498,2209,2795,3978,14106,11548,8334,5584,11374,10482,7760,16042,17793,18711,2710,14096,18522,531,2064,16584,15515,8442,18736,6534,3601,816,9585,14899,8425,11350,188,13232,19713,15714,9607,5967,5722,12784,4319,7299,2784,15952,18666,1450,6112,10996,16144,17626,15371,7944,11100,8765,11096,9717,16377,10668,9468,1166,12505,9383,16707,5448,11270,9400,6265,4798,2197,17602,11855,5557,13654,821,17545,11451,17123,1898,17958,6216,14296,8661,6112,14118,12184,12210,11261,12400,8552,17377,14242,8608,9544,10249,8511,1399,15896,6643,12425,6213,2260,6118,4529,504,18905,10811,7247,13308,9398,6245,1573,12528,3777,10387,13184,10535,1799,11183,2353,17808,9941,507,16228,19921,7030,11671,5100,13781,13540,13243,1905,6849,3024,12208,5852,19622,17990,5451,10548,1216,13084,9945,13917,9891,12040,6510,14936,5641,628,7629,1193,7630,1782,5399,4429,17663,18783,9709,6889,18058,12119,6738,13263,13399,6742,3157,18844,524,7319,11360,12585,15582,1785,6025,18923,17066,19106,12502,7345,5644,9378,15468,10716,4475,16370,18772,14872,9277,18015,17953,4052,11734,15389,17663,1390,17275,2317,18653,10020,338,13452,18570,3092,8927,3018,16610,267,10832,11122,12586,1162,11641,526,3216,3379,1791,19601,5778,14792,9907,4514,4200,5599,1911,8470,7165,1774,5626,16289,1695,19591,3222,15913,16493,5145,9296,6481,17801,1718,13341,3538,19558,14279,5907,10072,9572,4426,18388,5090,16252,11514,10833,10737,7526,13105,6792,15561,7284,17862,10283,14088,6596,19749,4827,8876,19027,535,1156],
                expected=True
            )
        ]

        s = Solution()
        for tc in testcases:
            got = s.canJump(tc.nums)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(
                    tc.name, tc.expected, got
                ),
            )

def main():
    s = Solution()
    print(s)

if __name__ == '__main__':
    main()
    unittest.main()