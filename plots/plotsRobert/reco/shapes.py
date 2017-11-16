#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi, atan2, cosh, sinh
from RootTools.core.standard      import *
from TopEFT.tools.user            import plot_directory
from TopEFT.tools.helpers         import deltaR, deltaPhi, getObjDict, getVarValue
from TopEFT.tools.objectSelection import getFilterCut, isBJet
from TopEFT.tools.cutInterpreter  import cutInterpreter

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--signal',             action='store',      default=None,            nargs='?', choices=[None, "ewkDM_dipoleEllipsis", 'ewkDM_currentEllipsis'], help="Add signal to plot")
argParser.add_argument('--onlyTTZ',            action='store_true', default=False,           help="Plot only ttZ")
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--reweightPtZToSM',                         action='store_true',     help='Reweight Pt(Z) to the SM for all the signals?', )
argParser.add_argument('--plot_directory',     action='store',      default='80X_v5')
argParser.add_argument('--selection',          action='store',      default='lepSelTTZ-njet3p-btag1p-onZ')
argParser.add_argument('--badMuonFilters',     action='store',      default="Summer2016",  help="Which bad muon filters" )
args = argParser.parse_args()

#
# Logger
#
import TopEFT.tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"
if args.badMuonFilters!="Summer2016": args.plot_directory += "_badMuonFilters_"+args.badMuonFilters
if args.signal:                       args.plot_directory += "_signal_"+args.signal
if args.onlyTTZ:                      args.plot_directory += "_onlyTTZ"
if args.reweightPtZToSM:              args.plot_directory += "_reweightPtZToSM"

#
# Make samples, will be searched for in the postProcessing directory
#
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

postProcessing_directory = "TopEFT_PP_v11/trilep/"
from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *

signals = [ewkDM_TTZToLL_LO, ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2]
ewkDM_TTZToLL_LO.style = styles.lineStyle( ROOT.kBlack, width=2, dotted=False, dashed=False )
ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2.style = styles.lineStyle( ROOT.kBlue,   width=2, dotted=False )

#if args.signal.startswith( "ewkDM" ):
#    postProcessing_directory = "TopEFT_PP_v11/trilep/"
#    from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *
#    ewkDM_0     = ewkDM_TTZToLL_LO
#    ewkDM_1     = ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2 
#
#    ewkDM_0.style = styles.lineStyle( ROOT.kBlack, width=3, dotted=False, dashed=False )
#    ewkDM_1.style = styles.lineStyle( ROOT.kBlack, width=3, dotted=True )
#
##    ewkDM_dipole_2     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767
##    ewkDM_dipole_3     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767
##    ewkDM_dipole_4     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767
##    ewkDM_dipole_5     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25
##    ewkDM_dipole_6     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25
##    ewkDM_dipole_7     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25
##    ewkDM_dipole_8     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25
#
##    ewkDM_dipole_2.style = styles.lineStyle( ROOT.kMagenta, width=3)
##    ewkDM_dipole_3.style = styles.lineStyle( ROOT.kMagenta, width=3, dotted=True)
##    ewkDM_dipole_4.style = styles.lineStyle( ROOT.kMagenta, width=3, dashed=True)
##
##    ewkDM_dipole_5.style = styles.lineStyle( ROOT.kBlue, width=3)
##    ewkDM_dipole_6.style = styles.lineStyle( ROOT.kBlue, width=3, dotted=True)
##    ewkDM_dipole_7.style = styles.lineStyle( ROOT.kGreen+2, width=3)
##    ewkDM_dipole_8.style = styles.lineStyle( ROOT.kGreen+2, width=3, dotted=True)
##
##    ewkDM_current_0 = ewkDM_ttZ_ll_DC1A_0p50_DC1V_0p50
##    ewkDM_current_1 = ewkDM_ttZ_ll_DC1A_0p50_DC1V_m1p00
##    ewkDM_current_0.style = styles.lineStyle( ROOT.kBlue)
##    ewkDM_current_1.style = styles.lineStyle( ROOT.kGreen+2)
#
#    if args.signal == 'ewkDM_dipoleEllipsis':
#        signals = [ewkDM_dipole_2,ewkDM_dipole_3,ewkDM_dipole_4,ewkDM_dipole_5,ewkDM_dipole_6,ewkDM_dipole_7,ewkDM_dipole_8]
#    elif args.signal == 'ewkDM_currentEllipsis':
#        signals = [ewkDM_current_0, ewkDM_current_1]
#    else:
#        raise ValueError
#else:
#    signals = []

def getter( var ):
    return lambda event, sample: getattr( event, var )

# define 3l selections
def getLeptonSelection( mode ):
  if   mode=="mumumu": return "nGoodMuons==3&&nGoodElectrons==0"
  elif mode=="mumue":  return "nGoodMuons==2&&nGoodElectrons==1"
  elif mode=="muee":   return "nGoodMuons==1&&nGoodElectrons==2"
  elif mode=="eee":    return "nGoodMuons==0&&nGoodElectrons==3"
  elif mode=='all':    return "nGoodMuons+nGoodElectrons==3"

# backgrounds / mc
if args.onlyTTZ:
    mc = [ TTZtoLLNuNu ]
else:
    mc = [ TTZtoLLNuNu , TTX, WZ, TTW, TZQ, rare ]#, nonprompt ]

for sample in mc: sample.style = styles.fillStyle(sample.color)

# reweighting 
if args.reweightPtZToSM:
    sel_string = "&&".join([getFilterCut(isData=False, badMuonFilters = args.badMuonFilters), getLeptonSelection('all'), cutInterpreter.cutString(args.selection)])
    TTZ_ptZ = TTZtoLLNuNu.get1DHistoFromDraw("Z_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
    TTZ_ptZ.Scale(1./TTZ_ptZ.Integral())

    def get_reweight( var, histo ):

        def reweight(event, sample):
            i_bin = histo.FindBin(getattr( event, var ) )
            return histo.GetBinContent(i_bin)

        return reweight

    for signal in signals:
        logger.info( "Computing PtZ reweighting for signal %s", signal.name )
        signal_ptZ = signal.get1DHistoFromDraw("Z_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
        signal_ptZ.Scale(1./signal_ptZ.Integral())

        signal.reweight_ptZ_histo = TTZ_ptZ.Clone()
        signal.reweight_ptZ_histo.Divide(signal_ptZ)

        signal.weight = get_reweight( "Z_pt", signal.reweight_ptZ_histo )

# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F]", "njet/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I", 
                    "Z_phi/F", "Z_eta/F", "Z_pt/F", "Z_mass/F", "Z_lldPhi/F", "Z_lldR/F"
                    ]
sequence = []

def extra_observables( event, sample ):

    # Z boson and l3 (convinience)
    Z_3D   = ROOT.TVector3( event.Z_pt*cos(event.Z_phi), event.Z_pt*sin(event.Z_phi), event.Z_pt*sinh(event.Z_eta) )
    l3_3D  = ROOT.TVector3( event.lep_pt[event.nonZ_l1_index]*cos(event.lep_phi[event.nonZ_l1_index]), event.lep_pt[event.nonZ_l1_index]*sin(event.lep_phi[event.nonZ_l1_index]), event.lep_pt[event.nonZ_l1_index]*sinh(event.lep_eta[event.nonZ_l1_index]) )
    l3_pt  = event.lep_pt[event.nonZ_l1_index] 
    l3_phi = event.lep_phi[event.nonZ_l1_index] 
    l3_eta = event.lep_eta[event.nonZ_l1_index] 

    Z_2D        = ROOT.TVector2( Z_3D[0],  Z_3D[1]  )
    n_Z_2D      = ROOT.TVector2( cos(event.Z_phi), sin(event.Z_phi) )
    n_orth_Z_2D = ROOT.TVector2( -sin(event.Z_phi), cos(event.Z_phi) )
    l3_2D       = ROOT.TVector2( l3_3D[0], l3_3D[1] )

    # me_x,y
    met_2D = ROOT.TVector2( event.met_pt*cos(event.met_phi), event.met_pt*sin(event.met_phi) )

    # get jets
    jetVars     = ['eta','pt','phi','btagCSV']
    jets        = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'njet')))]
    jets.sort( key = lambda l:-l['pt'] )

    bJets       = filter(lambda j: isBJet(j, tagger = 'CSVv2') and abs(j['eta'])<=2.4, jets)
    nonBJets    = filter(lambda j: not ( isBJet(j, tagger = 'CSVv2') and abs(j['eta'])<=2.4 ), jets)

    # take highest-pT b-jet, supplement by non-bjets if there are less than two
    bj0, bj1 = (bJets+nonBJets)[:2]
    bj0_3D = ROOT.TVector3( bj0['pt']*cos(bj0['phi']), bj0['pt']*sin(bj0['phi']), bj0['pt']*sinh(bj0['eta']) )
    bj1_3D = ROOT.TVector3( bj1['pt']*cos(bj1['phi']), bj1['pt']*sin(bj1['phi']), bj1['pt']*sinh(bj1['eta']) )
    bj0_2D = ROOT.TVector2( bj0_3D[0], bj0_3D[1] )
    bj1_2D = ROOT.TVector2( bj1_3D[0], bj1_3D[1] )

    # resolve pairing ambiguity of bjets to top candidates by maximising the resulting sum-pT (the miracle of M3) 
    if (bj0_2D + l3_2D + met_2D).Mod2() > ( bj1_2D + l3_2D + met_2D).Mod2():
        blep, bhad        = bj0,    bj1
        blep_2D, bhad_2D  = bj0_2D, bj1_2D
        blep_3D, bhad_3D  = bj0_3D, bj1_3D
    else:
        blep, bhad        = bj1,    bj0
        blep_2D, bhad_2D  = bj1_2D, bj0_2D
        blep_3D, bhad_3D  = bj1_3D, bj0_3D

    event.blep_pt = blep['pt'] 

    # ST observables
    event.ST = l3_pt + event.met_pt  # traditional (1l SUS)
    event.St = l3_pt + event.met_pt + event.blep_pt # scalar sum pt of the leptonic top candidate

    # MT observables
    event.mT = sqrt(  2*event.met_pt*l3_pt*(1 - cos(event.met_phi - l3_phi))) # transverse mass of leptonic W candidate
    event.mt = sqrt(  2*event.met_pt*l3_pt*(1 - cos(event.met_phi - l3_phi)) \
                    + 2*blep['pt']*l3_pt*(cosh(blep['eta'] - l3_eta)-cos(blep['phi'] - l3_phi))
                    + 2*event.met_pt*blep['pt']*(1-cos(event.met_phi - blep['phi'])) ) # transverse mass of the leptonic top

    # variables with 2D vectors  
    for fname, f in [\
        #[ 'dPhiZ',    lambda vec: ROOT.TVector2.DeltaPhi( vec, Z_2D )],
        [ 'absDPhiZ', lambda vec: abs(ROOT.TVector2.DeltaPhi( vec, Z_2D ))],
        [ 'projZ',    lambda vec: vec* n_Z_2D ],
        #[ 'dotZ',     lambda vec: vec.Dot( Z_2D )  )],
        [ 'projorthZ',lambda vec: vec*n_orth_Z_2D ],
        ]:
        for vname, v in [
            [ "met",          met_2D],
            [ "met_blep",     met_2D + blep_2D],
            [ "met_l3",       met_2D + l3_2D],
            [ "l3",           l3_2D],
            [ "blep",         blep_2D],
            [ "l3_blep",      l3_2D+blep_2D],
            [ "met_l3_blep",  l3_2D+blep_2D+met_2D],
            ]:
                #varname = "%s_%s"%( fname, vname )
                setattr( event, "%s_%s"%( fname, vname ), f(v) )

    # variables with 3D vectors  
    for fname, f in [ 
        [ 'dRZ',    lambda vec: ROOT.TVector3.DeltaR( vec, Z_3D )],
        ]:
        for vname, v in [
            [ "l3",         l3_3D],
            [ "blep",       blep_3D],
            [ "l3_blep",    l3_3D+blep_3D],
            ]:
                #varname = "%s_%s"%( fname, vname )
                setattr( event, "%s_%s"%( fname, vname ), f(v) )

sequence.append( extra_observables )

#
# Text on the plots
#
def drawObjects( lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Simulation'), 
      (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots, mode):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.plot_directory, mode + ("_log" if log else ""), args.selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      
      plotting.draw(plot,
	    plot_directory = plot_directory_,
	    #ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = {},
	    legend = [ (0.15,0.9-0.025*sum(map(len, plot.histos)),0.9,0.9), 2],
	    drawObjects = drawObjects( lumi_scale ),
        copyIndexPHP = False
      )

#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['mumumu','mumue','muee', 'eee']
for index, mode in enumerate(allModes):
    yields[mode] = {}

    lumi_scale = 35.9
    weight_ = lambda event, sample: event.weight

    for sample in mc + signals:
      sample.scale          = lumi_scale
      #sample.read_variables = ['reweightTopPt/F','reweightDilepTriggerBackup/F','reweightLeptonSF/F','reweightBTag_SF/F','reweightPU36fb/F', 'nTrueInt/F', 'reweightLeptonTrackingSF/F']
      #sample.weight         = lambda event, sample: event.reweightTopPt*event.reweightBTag_SF*event.reweightLeptonSF*event.reweightDilepTriggerBackup*event.reweightPU36fb*event.reweightLeptonTrackingSF
      sample.setSelectionString([getFilterCut(isData=False, badMuonFilters = args.badMuonFilters), getLeptonSelection(mode)])

      stack = Stack(mc)

    stack.extend( [ [s] for s in signals ] )

    if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 1 )

    # Use some defaults
    Plot.setDefaults(stack = stack, weight = weight_, selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper')

    plots = []
    
    plots.append(Plot(
      name = 'yield', texX = 'yield', texY = 'Number of Events',
      attribute = lambda event, sample: 0.5 + index,
      binning=[4, 0, 4],
    ))
    
    plots.append(Plot(
      name = 'nVtxs', texX = 'vertex multiplicity', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nVert/I" ),
      binning=[50,0,50],
    ))
    
    plots.append(Plot(
        texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_pt/F" ),
        binning=[400/20,0,400],
    ))
    
    plots.append(Plot(
        texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_phi/F" ),
        binning=[10,-pi,pi],
    ))
    
    plots.append(Plot(
        texX = 'p_{T}(Z) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[25,0,500],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_coarse', texX = 'p_{T}(Z) (GeV)', texY = 'Number of Events / 40 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[20,0,800],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_superCoarse', texX = 'p_{T}(Z) (GeV)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[3,0,800],
    ))

    plots.append(Plot(
        name = 'Z_pt_reweighting', texX = 'p_{T}(Z) (GeV)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[20,0,1000],
    ))

    plots.append(Plot(
        name = 'Z_eta', texX = '#eta(Z) ', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_eta/F" ),
        binning=[30,-3,3],
    ))
    
    plots.append(Plot(
        texX = '#Delta#phi(ll)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_lldPhi/F" ),
        binning=[10,0,pi],
    ))

    plots.append(Plot(
        texX = '#DeltaR(ll)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_lldR/F" ),
        binning=[10,0,4],
    ))
    plots.append(Plot(
        name = "Z_lldEta",
        texX = '#Delta #eta(ll)', texY = 'Number of Events',
        attribute = lambda event, sample: abs(event.lep_eta[event.Z_l1_index] - event.lep_eta[event.Z_l2_index]),
        binning=[10,0,4],
    ))

    plots.append(Plot(
        name = "lZ1_pt",
        texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning=[30,0,300],
    ))
    
    plots.append(Plot(
        name = 'lZ1_pt_ext', texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning=[20,40,440],
    ))
    
    plots.append(Plot(
        name = "lZ2_pt",
        texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning=[30,0,300],
    ))
    
    plots.append(Plot(
        name = 'lZ2_pt_ext', texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning=[20,40,440],
    ))
    
    plots.append(Plot(
        name = 'lnonZ1_pt',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[30,0,300],
    ))

    plots.append(Plot(
        name = 'lnonZ1_pt_ext',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[12,0,180],
    ))
    
    
    plots.append(Plot(
        texX = 'M(ll) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "Z_mass/F" ),
        binning=[10,81,101],
    ))

    plots.append(Plot(
        name = "Z_mass_wide",
        texX = 'M(ll) (GeV)', texY = 'Number of Events / 2 GeV',
        attribute = TreeVariable.fromString( "Z_mass/F" ),
        binning=[50,20,120],
    ))
    
    plots.append(Plot(
      texX = 'N_{jets}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "njet/I" ),
      binning=[5,2.5,7.5],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet1_pt', attribute = lambda event, sample: event.jet_pt[0],
      binning=[600/30,0,600],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(2nd leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet2_pt', attribute = lambda event, sample: event.jet_pt[1],
      binning=[600/30,0,600],
    ))


    ###############################################################################
    plots.append(Plot(
      name = 'mT', texX = 'm_{T}(l_{3},E_{T}^{miss}) (GeV)', texY = 'Number of Events / 5 GeV',
      attribute = lambda event, sample: event.mT,
      binning=[30, 0, 150],
    ))
    
    plots.append(Plot(
      name = 'mt', texX = 'm_{T}(b_{lep},l_{3},E_{T}^{miss}) (GeV)', texY = 'Number of Events / 12 GeV',
      attribute = lambda event, sample: event.mt,
      binning=[30, 0, 360],
    ))

    plots.append(Plot(
      name = 'ST', texX = 'S_{T} (GeV)', texY = 'Number of Events / 20 GeV',
      attribute = lambda event, sample: event.ST,
      binning=[30, 0, 600],
    ))
    
    plots.append(Plot(
      name = 'St', texX = 'S_{t} (GeV)', texY = 'Number of Events / 30 GeV',
      attribute = lambda event, sample: event.St,
      binning=[30, 0, 900],
    ))

    for fname, ftex, binning in [\
        [ 'absDPhiZ', '|#Delta#phi|(Z,%s)',   [20, 0, pi] ],
        [ 'projZ',    'n_{Z} . (%s)',         [20,0,400]],
        [ 'projorthZ','n_{Z,#perp } . (%s)', [20,0,400]],
        #[ 'dotZ',     lambda vec: vec.Dot( Z_2D )  )],
        #[ 'projorthZ',lambda vec: vec.Dot( n_orth_Z_2D )  )],
        ]:

        for vname, vtex in [\
                [ "met",         "E_{T}^{miss}"], 
                [ "met_blep",    "E_{T}^{miss}+b_{lep}"],
                [ "met_l3",      "E_{T}^{miss}+l_{3}"],
                [ "l3",          "l_{3}"],
                [ "blep",        "b_{lep}"], 
                [ "l3_blep",     "l_{3}+b_{lep}"],
                [ "met_l3_blep", "E_{T}^{miss}+l_{3}+b_{lep}"],
            ]:

            plots.append(Plot(
              name = '%s_%s'%(fname, vname), texX = ftex%vtex, texY = 'Number of Events',
              attribute = getter( "%s_%s"%(fname, vname) ),
              binning   = binning,
            ))
    for fname, ftex, binning in [\
        [ 'dRZ', '|#Delta R|(Z,%s)',   [30, 0, 6] ],
        ]:

        for vname, vtex in [\
                [ "l3",          "l_{3}"],
                [ "blep",        "b_{lep}"], 
                [ "l3_blep",     "l_{3}+b_{lep}"],
            ]:

            plots.append(Plot(
              name = '%s_%s'%(fname, vname), texX = ftex%vtex, texY = 'Number of Events',
              attribute = getter( "%s_%s"%(fname, vname) ),
              binning   = binning,
            ))

    plotting.fill(plots, read_variables = read_variables, sequence = sequence)

    # Get normalization yields from yield histogram
    for plot in plots:
      if plot.name == "yield":
        for i, l in enumerate(plot.histos):
          for j, h in enumerate(l):
            yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
            h.GetXaxis().SetBinLabel(1, "#mu#mu#mu")
            h.GetXaxis().SetBinLabel(2, "#mu#mue")
            h.GetXaxis().SetBinLabel(3, "#muee")
            h.GetXaxis().SetBinLabel(4, "eee")
    #if args.noData: yields[mode]["data"] = 0

    yields[mode]["MC"] = sum(yields[mode][s.name] for s in mc)
    #dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    drawPlots(plots, mode)
    allPlots[mode] = plots

# Add the different channels into SF and all
for mode in ["comb1","comb2","all"]:
    yields[mode] = {}
    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in ['eee','muee','mumue', 'mumumu'])
        except: yields[mode][y] = 0
    
    for plot in allPlots['mumumu']:
        if mode=="comb1":
            tmp = allPlots['mumue']
        elif mode=="comb2":
            tmp = allPlots['muee']
        else:
            tmp = allPlots['eee']
        for plot2 in (p for p in tmp if p.name == plot.name):
            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
                    if i==k:
                        j.Add(l)
    
    if mode == "all": drawPlots(allPlots['mumumu'], mode)

logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )
