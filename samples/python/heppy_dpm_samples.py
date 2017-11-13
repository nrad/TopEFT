'''
Extract cmg samples from dpm'''

if __name__ == '__main__':
    # Parse args if main
    maxN_def = -1
    def get_parser():
        ''' Argument parser for post-processing module.
        '''
        import argparse
        argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")
        argParser.add_argument('--logLevel', action='store', nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'DEBUG', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )
        argParser.add_argument('--overwrite', action='store_true', default=False, help="Overwrite cache?" )
        argParser.add_argument('--nomultithreading', action='store_true', default=False, help="No multithreading?" )
        argParser.add_argument('--maxN', action='store', type=int, default=maxN_def, help="Overwrite cache?" )

        return argParser

    options = get_parser().parse_args()

    # Logging
    import TopEFT.tools.logger as logger_
    logger = logger_.get_logger(options.logLevel, logFile = None )

    overwrite = options.overwrite
    maxN = options.maxN

else:
    # Logging
    import logging
    logger = logging.getLogger(__name__)

    overwrite = False 
    maxN =      -1

# TopEFT
from TopEFT.samples.walk_dpm import walk_dpm

# Standard imports
import os
import pickle

class heppy_mapper:

    def __init__(self, heppy_samples, dpm_directories, cache_file):
        # Read cache file, if exists
        if os.path.exists( cache_file ) and not overwrite:
            self.sample_map = pickle.load( file(cache_file) )
            logger.info( "Loaded cache file %s" % cache_file )
        else:
            logger.info( "Cache file %s not found. Recreate map.", cache_file)
            logger.info( "Check proxy.")

            # Proxy certificate
            from RootTools.core.helpers import renew_proxy
            # Make proxy in afs to allow batch jobs to run
            proxy_path = os.path.expandvars('$HOME/private/.proxy')
            proxy = renew_proxy( proxy_path )
            logger.info( "Using proxy %s"%proxy )

            # Read dpm directories
            self.cmg_directories = {}
            for data_path in dpm_directories:
                logger.info( "Walking dpm directory %s", data_path )
                walker = walk_dpm( data_path )
                self.cmg_directories[ data_path ] = walker.walk_dpm_cmgdirectories('.',  maxN = maxN )
                
                #del walker

            logger.info( "Now mapping directories to heppy samples" )
            for heppy_sample in heppy_samples:
                heppy_sample.candidate_directories = []
                pd, era = heppy_sample.dataset.split('/')[1:3]
                for data_path in self.cmg_directories.keys():
                    for dpm_directory in self.cmg_directories[data_path].keys():
                        if not ('/%s/'%pd in dpm_directory):
                            logger.debug( "/%s/ not in dpm_directory %s", pd, dpm_directory )
                            continue
                        if not ('/'+era in dpm_directory):
                            logger.debug( "/%s not in dpm_directory %s", era, dpm_directory )
                            continue
                        heppy_sample.candidate_directories.append([data_path, dpm_directory])
                        logger.debug( "heppy sample %s in %s", heppy_sample.name, dpm_directory)
                logger.info(  "Found heppy sample %s in %i directories.", heppy_sample.name, len(heppy_sample.candidate_directories) ) 

            # Merge
            from RootTools.core.Sample import Sample
            logger.info( "Now making new sample map from %i directories and for %i heppy samples to be stored in %s", len(dpm_directories), len(heppy_samples), cache_file )
            self.sample_map = {}
            for heppy_sample in heppy_samples:
                if len(heppy_sample.candidate_directories)==0:
                    logger.info("No directory found for %s", heppy_sample.name)
                else:
                    normalization, files = walker.combine_cmg_directories(\
                            cmg_directories = {dpm_directory:self.cmg_directories[data_path][dpm_directory] for data_path, dpm_directory in heppy_sample.candidate_directories }, 
                            multithreading = not options.nomultithreading, 
                        )
                    logger.info( "Sample %s: Found a total of %i files with normalization %3.2f", heppy_sample.name, len(files), normalization)
                    self.sample_map[heppy_sample] = Sample.fromFiles(
                        heppy_sample.name, 
                        files = ['root://hephyse.oeaw.ac.at/'+f for f in files],
                        normalization = normalization, 
                        treeName = 'tree', isData = heppy_sample.isData, maxN = maxN)
                    
                    logger.info("Combined %i directories for sample %s to a total of %i files with normalization %3.2f", len(heppy_sample.candidate_directories), heppy_sample.name, len(files), normalization)

            # Store cache file
            dir_name = os.path.dirname( cache_file ) 
            if len(self.sample_map.keys())>0:
                if not os.path.exists( dir_name ): os.makedirs( dir_name )
                pickle.dump( self.sample_map, file( cache_file, 'w') )
                logger.info( "Created MC sample cache %s", cache_file )
            else:
                logger.info( "Skipping to write %s because map is empty.", cache_file )

    @property                
    def heppy_sample_names( self ):
        return [s.name for s in self.sample_map.keys()]

    def from_heppy_sample( self, heppy_sample, maxN = -1):
        if self.sample_map.has_key( heppy_sample ):
            res = self.sample_map[heppy_sample]
            if maxN>0: res.files = res.files[:maxN]
            res.heppy = heppy_sample
            return res
    def from_heppy_samplename( self, heppy_samplename, maxN = -1):
        for heppy_sample in self.sample_map.keys():
            if heppy_samplename==heppy_sample.name:
                res = self.sample_map[heppy_sample]
                if maxN>0: res.files = res.files[:maxN]
                res.heppy = heppy_sample
                return res
        
# Proxy certificate
from RootTools.core.helpers import renew_proxy
# Make proxy in afs to allow batch jobs to run
proxy_path = os.path.expandvars('$HOME/private/.proxy')
proxy = renew_proxy( proxy_path )
logger.info( "Using proxy %s"%proxy )

# Moriond MC
mc_cache_file = '/afs/hephy.at/data/dspitzbart01/TopEFT/dpm_sample_caches/80X_MC_Summer16_2l_v9+v10+WJets1l.pkl'
#subdirs by hand ... skipping DY until it's complete
robert_v9 = ['/dpm/oeaw.ac.at/home/cms/store/user/schoef/cmgTuples/80X_2l_v9/%s' % s for s in [\
  'DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_80X_2l_v9',
  'DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_80X_2l_v9',
  'DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_80X_2l_v9',
  'DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
  'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_80X_2l_v9',
  'DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_80X_2l_v9',
  'DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_80X_2l_v9',
  'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8',
  'ST_tWll_5f_LO_13TeV-MadGraph-pythia8',
  'TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8',
  'THQ_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1',
  'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
  'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
  'TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8',
  'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
  'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
  'TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8',
  'WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
  'WWTo2L2Nu_DoubleScattering_13TeV-pythia8',
  'WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
  'WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
  'WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
  'WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
  'WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8',
  'ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
  'ZZTo4L_13TeV_powheg_pythia8',
  'ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
  'tZq_ll_4f_13TeV-amcatnlo-pythia8',
  'ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8',
  'ttZJets_13TeV_madgraphMLM',
    ] ]

robert_v10 = ['/dpm/oeaw.ac.at/home/cms/store/user/schoef/cmgTuples/80X_2l_v10/%s' % s for s in [\
  'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1_80X_2l_v10',
  'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1_80X_2l_v10',
  'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1_80X_2l_v10',
  'DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1_80X_2l_v10'
  'DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1_80X_2l_v10',
  'DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1_80X_2l_v10', 
    ]]
daniel_v10 = [
    '/dpm/oeaw.ac.at/home/cms/store/user/dspitzba/cmgTuples/80X_1l_v10/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    '/dpm/oeaw.ac.at/home/cms/store/user/dspitzba/cmgTuples/80X_1l_v10/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_80X_1l_v10/171112_173049'
    ]
mc_Moriond_dpm_directories = robert_v9 + robert_v10 + daniel_v10
from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import mcSamples as heppy_mc_Moriond_samples
#mc_heppy_mapper = heppy_mapper( heppy_mc_Moriond_samples, mc_Moriond_dpm_directories, mc_cache_file)

# Data ReminiAOD
data_cache_file = '/afs/hephy.at/data/dspitzbart01/TopEFT/dpm_sample_caches/80X_2l_v6_data.pkl'
def_robert = ["/dpm/oeaw.ac.at/home/cms/store/user/dspitzba/cmgTuples/80X_2l_v6"]
data_dpm_directories = def_robert
from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import dataSamples as heppy_data_samples
data_03Feb2017_heppy_mapper = heppy_mapper( heppy_data_samples, data_dpm_directories, data_cache_file)

# Data ReminiAOD
MET_data_cache_file = '/afs/hephy.at/data/rschoefbeck01/TopEFT/dpm_sample_caches/80X_1l_v10_MET_data.pkl'
def_robert = ["/dpm/oeaw.ac.at/home/cms/store/user/schoef/cmgTuples/80X_1l_v10/MET"]
data_dpm_directories = def_robert
from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import dataSamples as heppy_data_samples
MET_data_03Feb2017_heppy_mapper = heppy_mapper( heppy_data_samples, data_dpm_directories, MET_data_cache_file)

# Private signal MC
signal_cache_file = '/afs/hephy.at/data/dspitzbart01/TopEFT/dpm_sample_caches/80X_signal_Summer16_2l_v10.pkl'
robert = ['/dpm/oeaw.ac.at/home/cms/store/user/schoef/cmgTuples/80X_2l_v10', '/dpm/oeaw.ac.at/home/cms/store/user/dspitzba/cmgTuples/80X_2l_v10']
signal_dpm_directories = robert
from CMGTools.StopsDilepton.ewkDM_signals_RunIISummer16MiniAODv2 import signalSamples as heppy_signal_samples
signal_heppy_mapper = heppy_mapper( heppy_signal_samples, signal_dpm_directories, signal_cache_file)
