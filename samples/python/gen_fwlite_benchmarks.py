''' Benchmark samples for TopEFT (EDM)'''

# standard imports
import os

# RootTools
from RootTools.core.standard import *

#Top EFT
from TopEFT.Tools.user import results_directory 

# Robert GENSIM 0j benchmarks 09Nov17 (used for analysis development)
gen_dir = "/afs/hephy.at/data/rschoefbeck02/TopEFT/skims/gen/v2/"
ewkDM_ttZ_ll_gen                                             = Sample.fromDirectory("ewkDM_ttZ_ll_gen",                                                                           texName ="SM",                                                       directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS/")])
ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_0p500000                 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_0p500000",                                               texName ="C_{1,V}^{Z} = 0.5, C_{1,A}^{Z} = 0.5",    directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p500000_DC1V_0p500000/")])
ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_m1p000000                = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_m1p000000",                                              texName ="C_{1,V}^{Z} = -1, C_{1,A}^{Z} = 0.5",      directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p500000_DC1V_m1p000000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000",                                texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,A}^{Z} = 0.25",     directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000",                               texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,A}^{Z} = -0.25",     directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000",                                texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = 0.25",                                 directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000",                               texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = -0.25",                                  directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/")])
ewkDM_ttZ_ll_gen_DC2A_0p200000_DC2V_0p200000                 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC2A_0p200000_DC2V_0p200000",                                               texName ="C_{2,V}^{Z}=C_{2,A}^{Z}=0.2",                                 directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC2A_0p200000_DC2V_0p200000/")])
ewkDM_ttZ_ll_gen_DC1A_1p000000                               = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_1p000000",                                                             texName ="C_{1,A}^{Z} = 1",                                   directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_1p000000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700   = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700",   texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = 0.1767, C_{2,A}^{Z} = 0.1767",                                  directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700",  texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = -0.1767, C_{2,A}^{Z} = 0.1767",                                   directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700",  texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = 0.1767, C_{2,A}^{Z} = -0.1767",                                 directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700", texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = -0.1767, C_{2,A}^{Z} = -0.1767",                                 directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/")])

HEL_UFO_ttZ_ll_gen_cuW_0p100000                              = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_0p100000",                                                                 directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_0p100000/")])
HEL_UFO_ttZ_ll_gen_cuW_0p200000                              = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_0p200000",                                                                 directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_0p200000/")])
HEL_UFO_ttZ_ll_gen_cuW_0p300000                              = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_0p300000",                                                                 directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_0p300000/")])
HEL_UFO_ttZ_ll_gen_cuW_m0p100000                             = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_m0p100000",                                                                directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_m0p100000/")])
HEL_UFO_ttZ_ll_gen_cuW_m0p200000                             = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_m0p200000",                                                                directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_m0p200000/")])
HEL_UFO_ttZ_ll_gen_cuW_m0p300000                             = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_m0p300000",                                                                directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_m0p300000/")])

# ttgamma but all W decays
ewkDMGZ_ttgamma_gen                             = Sample.fromDirectory("ewkDMGZ_ttgamma_gen",                               texName ="SM",                                                  directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS") ) 
ewkDMGZ_ttgamma_gen_DAG_m0p176700_DVG_m0p176700 = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_m0p176700_DVG_m0p176700",   texName ="C_{2,V}^{#gamma} = -0.1767, C_{2,A}^{#gamma} = -0.1767",directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_m0p176700_DVG_m0p176700") ) 
ewkDMGZ_ttgamma_gen_DAG_0p176700_DVG_0p176700   = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_0p176700_DVG_0p176700",     texName ="C_{2,V}^{#gamma} = 0.1767, C_{2,A}^{#gamma} = 0.1767", directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_0p176700_DVG_0p176700") ) 
ewkDMGZ_ttgamma_gen_DAG_0p176700_DVG_m0p176700  = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_0p176700_DVG_m0p176700",    texName ="C_{2,V}^{#gamma} = -0.1767, C_{2,A}^{#gamma} = 0.1767",directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_0p176700_DVG_m0p176700") )
ewkDMGZ_ttgamma_gen_DAG_m0p176700_DVG_0p176700  = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_m0p176700_DVG_0p176700",    texName ="C_{2,V}^{#gamma} = 0.1767, C_{2,A}^{#gamma} = -0.1767",directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_m0p176700_DVG_0p176700") )
ewkDMGZ_ttgamma_gen_DAG_m0p250000               = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_m0p250000",                 texName ="C_{2,A}^{#gamma} = -0.25",                            directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_m0p250000") )
ewkDMGZ_ttgamma_gen_DAG_m0p500000               = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_m0p500000",                 texName ="C_{2,A}^{#gamma} = -0.5",                             directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_m0p500000") )
ewkDMGZ_ttgamma_gen_DAG_0p250000                = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_0p250000",                  texName ="C_{2,A}^{#gamma} = 0.25",                            directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_0p250000") )
ewkDMGZ_ttgamma_gen_DAG_0p500000                = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_0p500000",                  texName ="C_{2,A}^{#gamma} = 0.5",                              directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_0p500000") )
ewkDMGZ_ttgamma_gen_DVG_0p250000                = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DVG_0p250000",                  texName ="C_{2,V}^{#gamma} = 0.25",                             directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DVG_0p250000") )
ewkDMGZ_ttgamma_gen_DVG_0p500000                = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DVG_0p500000",                  texName ="C_{2,V}^{#gamma} = 0.5",                              directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DVG_0p500000") )
ewkDMGZ_ttgamma_gen_DVG_m0p250000               = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DVG_m0p250000",                 texName ="C_{2,V}^{#gamma} = -0.25",                            directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DVG_m0p250000") )

# Daniel GENSIM 0j benchmarks Jan18 local production (for propaganda plots and reweighting studies)
gen_dir = "/afs/hephy.at/data/dspitzbart01/TopEFT/skims/gen/v2/"
dim6top_LO_ttZ_ll_ctZ_1p00_ctZI_1p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p00_ctZI_1p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p00_ctZI_1p00/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m2p00  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m2p00", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m0p80  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m0p80", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m1p60  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m1p60", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m2p00  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m2p00", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m0p40  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m0p40", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m0p80  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m0p80", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m0p40  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m0p40", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m1p60  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m1p60", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m1p20  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m1p20", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_0p80    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_0p80"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_0p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_0p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_1p60    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_1p60"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_2p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_2p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_0p40    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_0p40"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m1p60  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m1p60", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_0p80    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_0p80"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_1p20    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_1p20"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_1p60    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_1p60"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_0p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_0p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_1p20    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_1p20"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_0p40    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_0p40"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m0p40  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m0p40", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m1p60  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m1p60", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_0p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_0p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m1p20  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m1p20", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m0p40  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m0p40", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p40    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p40"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m1p20  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m1p20", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_0p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_0p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_1p20    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_1p20"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m2p00  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m2p00", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_0p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_0p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m0p80  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m0p80", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m2p00  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m2p00", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m1p20  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m1p20", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m0p80  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m0p80", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p80_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m0p40_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_0p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_0p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m1p20  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m1p20", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_2p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_2p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_0p80    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_0p80"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_2p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_2p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_1p60    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_1p60"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_1p20    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_1p20"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_0p40    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_0p40"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_1p60    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_1p60"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m2p00  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m2p00", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_2p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_2p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_0p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_0p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m2p00_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_0p80    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_0p80"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_0p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_0p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m0p80  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m0p80", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p60_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_1p60    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_1p60"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m1p60  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m1p60", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_0p40    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_0p40"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_0p40/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p80    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p80"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_2p00_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m0p40  = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m0p40", directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m1p60   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m1p60" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m1p60/")])
dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_m1p20_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_1p20    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_1p20"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_0p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_0p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p60_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m2p00   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m2p00" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m2p00/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_2p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_2p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_1p60    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_1p60"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_1p60/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m0p80   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m0p80" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_m0p80/")])
dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_2p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_2p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_2p00/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m0p40   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m0p40" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_m0p40/")])
dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_0p80    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_0p80"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_1p20_ctZI_0p80/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m1p20   = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m1p20" , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_m1p20/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_0p00    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_0p00"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_0p00/")])
dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_1p20    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_1p20"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p40_ctZI_1p20/")])
dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_0p40    = Sample.fromDirectory("dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_0p40"  , directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll_ctZ_0p80_ctZI_0p40/")])

allSamples_dim6top = [ locals()[x] for x in locals().keys() if x.startswith("dim6top") ]

