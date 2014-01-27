import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.load("RecoMET.Configuration.CaloTowersOptForMET_cff")

process.load("RecoMET.Configuration.RecoMET_cff")

process.load("RecoMET.Configuration.RecoHTMET_cff")

process.load("RecoMET.Configuration.RecoGenMET_cff")

process.load("RecoMET.Configuration.GenMETParticles_cff")

process.load("RecoMET.Configuration.RecoPFMET_cff")

process.load("RecoJets.Configuration.CaloTowersRec_cff")

process.load("Validation.RecoMET.METRelValForDQM_cff")

process.load("Configuration.StandardSequences.Geometry_cff")

process.load("Configuration.StandardSequences.MagneticField_cff")

process.load("DQMServices.Components.DQMStoreStats_cfi")

process.DQMStore = cms.Service("DQMStore")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string("PRE_ST61_V1::All")
process.source = cms.Source("PoolSource",
 #   debugFlag = cms.untracked.bool(True),
#    debugVebosity = cms.untracked.uint32(10),
    fileNames = cms.untracked.vstring(

	 '/store/relval/CMSSW_6_2_0_pre4/RelValTTbar/GEN-SIM-RECO/PRE_ST61_V1-v1/00000/0677C8FC-CA90-E211-9F9C-00259029D360.root'
    )


)


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


process.fileSaver = cms.EDAnalyzer("METFileSaver",
                                 OutputFile = cms.untracked.string('METTester.root')
) 
process.p = cms.Path(process.fileSaver*
                     #                     process.genMetTrue*
                     #                     process.genMetCalo*
                     #                     process.genMetCaloAndNonPrompt*
                     #                     process.tcMet*
                     process.METRelValSequence
)

process.dqmoffline_step = cms.Path(process.dqmStoreStats)

process.schedule = cms.Schedule(process.p,process.dqmoffline_step)


