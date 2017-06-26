from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'SMS_T1qqqq_fullsim'
config.General.workArea        = 'SMS_T1qqqq_fullsim_AODSIM'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'step3_T1qqqq_fullsim_AODSIM_cfg.py'
config.JobType.outputFiles = ['T1qqqq_fullsim_AODSIM.root',]

config.Data.inputDataset         = ''
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 100
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqq_fullsim_Madgraph_Pythia_AODSIM'

config.Site.storageSite = 'T2_UK_London_IC'
#config.Site.storageSite = 'T2_UK_SGrid_Bristol'
