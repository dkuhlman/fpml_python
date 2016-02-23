#!/usr/bin/env python

#
# Generated Tue Feb 23 09:02:22 2016 by generateDS.py version 2.19b.
#
# Command line options:
#   ('-f', '')
#   ('-o', 'fpml01/fpml_genericlib.py')
#   ('-s', 'fpml01/fpml_genericapp.py')
#   ('--super', 'fpml01/fpml_genericlib')
#   ('--member-specs', 'dict')
#   ('--export', 'write')
#
# Command line arguments:
#   fpml-master-schema-and-key-gen-scripts/src/schema/fpml-generic.xsd
#
# Command line:
#   ./generateDS.py -f -o "fpml01/fpml_genericlib.py" -s "fpml01/fpml_genericapp.py" --super="fpml01/fpml_genericlib" --member-specs="dict" --export="write" fpml-master-schema-and-key-gen-scripts/src/schema/fpml-generic.xsd
#
# Current working directory (os.getcwd()):
#   Test02
#

import sys
from lxml import etree as etree_

import fpml01/fpml_genericlib as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class GenericCommodityDeliveryPeriodSub(supermod.GenericCommodityDeliveryPeriod):
    def __init__(self, applicableDay=None, startTime=None, endTime=None):
        super(GenericCommodityDeliveryPeriodSub, self).__init__(applicableDay, startTime, endTime, )
supermod.GenericCommodityDeliveryPeriod.subclass = GenericCommodityDeliveryPeriodSub
# end class GenericCommodityDeliveryPeriodSub


class GenericCommodityGradeSub(supermod.GenericCommodityGrade):
    def __init__(self, commodityGradeScheme=None, valueOf_=None):
        super(GenericCommodityGradeSub, self).__init__(commodityGradeScheme, valueOf_, )
supermod.GenericCommodityGrade.subclass = GenericCommodityGradeSub
# end class GenericCommodityGradeSub


class GenericExerciseStyleSub(supermod.GenericExerciseStyle):
    def __init__(self, exerciseStyleScheme='http://www.fpml.org/coding-scheme/generic-exercise-style', valueOf_=None):
        super(GenericExerciseStyleSub, self).__init__(exerciseStyleScheme, valueOf_, )
supermod.GenericExerciseStyle.subclass = GenericExerciseStyleSub
# end class GenericExerciseStyleSub


class GenericProductExchangeRateSub(supermod.GenericProductExchangeRate):
    def __init__(self, quotedCurrencyPair=None, rate=None, spotRate=None, forwardPoints=None, pointValue=None, crossRate=None):
        super(GenericProductExchangeRateSub, self).__init__(quotedCurrencyPair, rate, spotRate, forwardPoints, pointValue, crossRate, )
supermod.GenericProductExchangeRate.subclass = GenericProductExchangeRateSub
# end class GenericProductExchangeRateSub


class GenericProductFeatureSub(supermod.GenericProductFeature):
    def __init__(self, featureScheme=None, valueOf_=None):
        super(GenericProductFeatureSub, self).__init__(featureScheme, valueOf_, )
supermod.GenericProductFeature.subclass = GenericProductFeatureSub
# end class GenericProductFeatureSub


class GenericProductQuotedCurrencyPairSub(supermod.GenericProductQuotedCurrencyPair):
    def __init__(self, currency1=None, currency2=None, quoteBasis=None):
        super(GenericProductQuotedCurrencyPairSub, self).__init__(currency1, currency2, quoteBasis, )
supermod.GenericProductQuotedCurrencyPair.subclass = GenericProductQuotedCurrencyPairSub
# end class GenericProductQuotedCurrencyPairSub


class OptionTypeSub(supermod.OptionType):
    def __init__(self, optionTypeScheme='http://www.fpml.org/coding-scheme/option-type', valueOf_=None):
        super(OptionTypeSub, self).__init__(optionTypeScheme, valueOf_, )
supermod.OptionType.subclass = OptionTypeSub
# end class OptionTypeSub


class TradeUnderlyer2Sub(supermod.TradeUnderlyer2):
    def __init__(self, id=None, floatingRate=None, fixedRate=None, exchangeRate=None, underlyingAsset=None, quotedCurrencyPair=None, referenceEntity=None, averagingMethod=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, dayCountFraction=None):
        super(TradeUnderlyer2Sub, self).__init__(id, floatingRate, fixedRate, exchangeRate, underlyingAsset, quotedCurrencyPair, referenceEntity, averagingMethod, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, dayCountFraction, )
supermod.TradeUnderlyer2.subclass = TradeUnderlyer2Sub
# end class TradeUnderlyer2Sub


class AccountSub(supermod.Account):
    def __init__(self, id=None, accountId=None, accountName=None, accountType=None, accountBeneficiary=None, servicingParty=None):
        super(AccountSub, self).__init__(id, accountId, accountName, accountType, accountBeneficiary, servicingParty, )
supermod.Account.subclass = AccountSub
# end class AccountSub


class AccountIdSub(supermod.AccountId):
    def __init__(self, accountIdScheme=None, valueOf_=None):
        super(AccountIdSub, self).__init__(accountIdScheme, valueOf_, )
supermod.AccountId.subclass = AccountIdSub
# end class AccountIdSub


class AccountNameSub(supermod.AccountName):
    def __init__(self, accountNameScheme=None, valueOf_=None):
        super(AccountNameSub, self).__init__(accountNameScheme, valueOf_, )
supermod.AccountName.subclass = AccountNameSub
# end class AccountNameSub


class AccountTypeSub(supermod.AccountType):
    def __init__(self, accountTypeScheme='http://www.fpml.org/coding-scheme/account-type', valueOf_=None):
        super(AccountTypeSub, self).__init__(accountTypeScheme, valueOf_, )
supermod.AccountType.subclass = AccountTypeSub
# end class AccountTypeSub


class ActionTypeSub(supermod.ActionType):
    def __init__(self, actionTypeScheme='http://www.fpml.org/coding-scheme/action-type', valueOf_=None):
        super(ActionTypeSub, self).__init__(actionTypeScheme, valueOf_, )
supermod.ActionType.subclass = ActionTypeSub
# end class ActionTypeSub


class AddressSub(supermod.Address):
    def __init__(self, streetAddress=None, city=None, state=None, country=None, postalCode=None):
        super(AddressSub, self).__init__(streetAddress, city, state, country, postalCode, )
supermod.Address.subclass = AddressSub
# end class AddressSub


class AdjustableDateSub(supermod.AdjustableDate):
    def __init__(self, id=None, unadjustedDate=None, dateAdjustments=None, adjustedDate=None):
        super(AdjustableDateSub, self).__init__(id, unadjustedDate, dateAdjustments, adjustedDate, )
supermod.AdjustableDate.subclass = AdjustableDateSub
# end class AdjustableDateSub


class AdjustableDate2Sub(supermod.AdjustableDate2):
    def __init__(self, id=None, unadjustedDate=None, dateAdjustments=None, dateAdjustmentsReference=None, adjustedDate=None):
        super(AdjustableDate2Sub, self).__init__(id, unadjustedDate, dateAdjustments, dateAdjustmentsReference, adjustedDate, )
supermod.AdjustableDate2.subclass = AdjustableDate2Sub
# end class AdjustableDate2Sub


class AdjustableDatesSub(supermod.AdjustableDates):
    def __init__(self, id=None, unadjustedDate=None, dateAdjustments=None, adjustedDate=None):
        super(AdjustableDatesSub, self).__init__(id, unadjustedDate, dateAdjustments, adjustedDate, )
supermod.AdjustableDates.subclass = AdjustableDatesSub
# end class AdjustableDatesSub


class AdjustableDatesOrRelativeDateOffsetSub(supermod.AdjustableDatesOrRelativeDateOffset):
    def __init__(self, adjustableDates=None, relativeDate=None):
        super(AdjustableDatesOrRelativeDateOffsetSub, self).__init__(adjustableDates, relativeDate, )
supermod.AdjustableDatesOrRelativeDateOffset.subclass = AdjustableDatesOrRelativeDateOffsetSub
# end class AdjustableDatesOrRelativeDateOffsetSub


class AdjustableOrAdjustedDateSub(supermod.AdjustableOrAdjustedDate):
    def __init__(self, id=None, unadjustedDate=None, dateAdjustments=None, adjustedDate=None):
        super(AdjustableOrAdjustedDateSub, self).__init__(id, unadjustedDate, dateAdjustments, adjustedDate, )
supermod.AdjustableOrAdjustedDate.subclass = AdjustableOrAdjustedDateSub
# end class AdjustableOrAdjustedDateSub


class AdjustableOrRelativeDateSub(supermod.AdjustableOrRelativeDate):
    def __init__(self, id=None, adjustableDate=None, relativeDate=None):
        super(AdjustableOrRelativeDateSub, self).__init__(id, adjustableDate, relativeDate, )
supermod.AdjustableOrRelativeDate.subclass = AdjustableOrRelativeDateSub
# end class AdjustableOrRelativeDateSub


class AdjustableOrRelativeDatesSub(supermod.AdjustableOrRelativeDates):
    def __init__(self, id=None, adjustableDates=None, relativeDates=None):
        super(AdjustableOrRelativeDatesSub, self).__init__(id, adjustableDates, relativeDates, )
supermod.AdjustableOrRelativeDates.subclass = AdjustableOrRelativeDatesSub
# end class AdjustableOrRelativeDatesSub


class AdjustableRelativeOrPeriodicDatesSub(supermod.AdjustableRelativeOrPeriodicDates):
    def __init__(self, id=None, adjustableDates=None, relativeDates=None, relativeDateSequence=None, periodicDates=None):
        super(AdjustableRelativeOrPeriodicDatesSub, self).__init__(id, adjustableDates, relativeDates, relativeDateSequence, periodicDates, )
supermod.AdjustableRelativeOrPeriodicDates.subclass = AdjustableRelativeOrPeriodicDatesSub
# end class AdjustableRelativeOrPeriodicDatesSub


class AdjustableRelativeOrPeriodicDates2Sub(supermod.AdjustableRelativeOrPeriodicDates2):
    def __init__(self, id=None, adjustableDates=None, relativeDates=None, periodicDates=None):
        super(AdjustableRelativeOrPeriodicDates2Sub, self).__init__(id, adjustableDates, relativeDates, periodicDates, )
supermod.AdjustableRelativeOrPeriodicDates2.subclass = AdjustableRelativeOrPeriodicDates2Sub
# end class AdjustableRelativeOrPeriodicDates2Sub


class AgreementTypeSub(supermod.AgreementType):
    def __init__(self, agreementTypeScheme=None, valueOf_=None):
        super(AgreementTypeSub, self).__init__(agreementTypeScheme, valueOf_, )
supermod.AgreementType.subclass = AgreementTypeSub
# end class AgreementTypeSub


class AgreementVersionSub(supermod.AgreementVersion):
    def __init__(self, agreementVersionScheme=None, valueOf_=None):
        super(AgreementVersionSub, self).__init__(agreementVersionScheme, valueOf_, )
supermod.AgreementVersion.subclass = AgreementVersionSub
# end class AgreementVersionSub


class AssetClassSub(supermod.AssetClass):
    def __init__(self, assetClassScheme='http://www.fpml.org/coding-scheme/asset-class', valueOf_=None):
        super(AssetClassSub, self).__init__(assetClassScheme, valueOf_, )
supermod.AssetClass.subclass = AssetClassSub
# end class AssetClassSub


class AutomaticExerciseSub(supermod.AutomaticExercise):
    def __init__(self, thresholdRate=None):
        super(AutomaticExerciseSub, self).__init__(thresholdRate, )
supermod.AutomaticExercise.subclass = AutomaticExerciseSub
# end class AutomaticExerciseSub


class AverageDailyTradingVolumeLimitSub(supermod.AverageDailyTradingVolumeLimit):
    def __init__(self, limitationPercentage=None, limitationPeriod=None):
        super(AverageDailyTradingVolumeLimitSub, self).__init__(limitationPercentage, limitationPeriod, )
supermod.AverageDailyTradingVolumeLimit.subclass = AverageDailyTradingVolumeLimitSub
# end class AverageDailyTradingVolumeLimitSub


class BeneficiarySub(supermod.Beneficiary):
    def __init__(self, routingIds=None, routingExplicitDetails=None, routingIdsAndExplicitDetails=None, beneficiaryPartyReference=None):
        super(BeneficiarySub, self).__init__(routingIds, routingExplicitDetails, routingIdsAndExplicitDetails, beneficiaryPartyReference, )
supermod.Beneficiary.subclass = BeneficiarySub
# end class BeneficiarySub


class BrokerConfirmationSub(supermod.BrokerConfirmation):
    def __init__(self, brokerConfirmationType=None):
        super(BrokerConfirmationSub, self).__init__(brokerConfirmationType, )
supermod.BrokerConfirmation.subclass = BrokerConfirmationSub
# end class BrokerConfirmationSub


class BrokerConfirmationTypeSub(supermod.BrokerConfirmationType):
    def __init__(self, brokerConfirmationTypeScheme='http://www.fpml.org/coding-scheme/broker-confirmation-type', valueOf_=None):
        super(BrokerConfirmationTypeSub, self).__init__(brokerConfirmationTypeScheme, valueOf_, )
supermod.BrokerConfirmationType.subclass = BrokerConfirmationTypeSub
# end class BrokerConfirmationTypeSub


class BusinessCenterSub(supermod.BusinessCenter):
    def __init__(self, businessCenterScheme='http://www.fpml.org/coding-scheme/business-center', id=None, valueOf_=None):
        super(BusinessCenterSub, self).__init__(businessCenterScheme, id, valueOf_, )
supermod.BusinessCenter.subclass = BusinessCenterSub
# end class BusinessCenterSub


class BusinessCentersSub(supermod.BusinessCenters):
    def __init__(self, id=None, businessCenter=None):
        super(BusinessCentersSub, self).__init__(id, businessCenter, )
supermod.BusinessCenters.subclass = BusinessCentersSub
# end class BusinessCentersSub


class BusinessCenterTimeSub(supermod.BusinessCenterTime):
    def __init__(self, hourMinuteTime=None, businessCenter=None):
        super(BusinessCenterTimeSub, self).__init__(hourMinuteTime, businessCenter, )
supermod.BusinessCenterTime.subclass = BusinessCenterTimeSub
# end class BusinessCenterTimeSub


class BusinessDayAdjustmentsSub(supermod.BusinessDayAdjustments):
    def __init__(self, id=None, businessDayConvention=None, businessCentersReference=None, businessCenters=None):
        super(BusinessDayAdjustmentsSub, self).__init__(id, businessDayConvention, businessCentersReference, businessCenters, )
supermod.BusinessDayAdjustments.subclass = BusinessDayAdjustmentsSub
# end class BusinessDayAdjustmentsSub


class BusinessUnitSub(supermod.BusinessUnit):
    def __init__(self, id=None, name=None, businessUnitId=None, contactInfo=None, country=None):
        super(BusinessUnitSub, self).__init__(id, name, businessUnitId, contactInfo, country, )
supermod.BusinessUnit.subclass = BusinessUnitSub
# end class BusinessUnitSub


class BusinessUnitRoleSub(supermod.BusinessUnitRole):
    def __init__(self, unitRoleScheme='http://www.fpml.org/coding-scheme/unit-role', valueOf_=None):
        super(BusinessUnitRoleSub, self).__init__(unitRoleScheme, valueOf_, )
supermod.BusinessUnitRole.subclass = BusinessUnitRoleSub
# end class BusinessUnitRoleSub


class CalculationAgentSub(supermod.CalculationAgent):
    def __init__(self, calculationAgentPartyReference=None, calculationAgentParty=None):
        super(CalculationAgentSub, self).__init__(calculationAgentPartyReference, calculationAgentParty, )
supermod.CalculationAgent.subclass = CalculationAgentSub
# end class CalculationAgentSub


class CashflowIdSub(supermod.CashflowId):
    def __init__(self, cashflowIdScheme=None, valueOf_=None):
        super(CashflowIdSub, self).__init__(cashflowIdScheme, valueOf_, )
supermod.CashflowId.subclass = CashflowIdSub
# end class CashflowIdSub


class CashflowNotionalSub(supermod.CashflowNotional):
    def __init__(self, id=None, currency=None, units=None, amount=None):
        super(CashflowNotionalSub, self).__init__(id, currency, units, amount, )
supermod.CashflowNotional.subclass = CashflowNotionalSub
# end class CashflowNotionalSub


class CashflowTypeSub(supermod.CashflowType):
    def __init__(self, cashflowTypeScheme='http://www.fpml.org/coding-scheme/cashflow-type', valueOf_=None):
        super(CashflowTypeSub, self).__init__(cashflowTypeScheme, valueOf_, )
supermod.CashflowType.subclass = CashflowTypeSub
# end class CashflowTypeSub


class CashSettlementReferenceBanksSub(supermod.CashSettlementReferenceBanks):
    def __init__(self, id=None, referenceBank=None):
        super(CashSettlementReferenceBanksSub, self).__init__(id, referenceBank, )
supermod.CashSettlementReferenceBanks.subclass = CashSettlementReferenceBanksSub
# end class CashSettlementReferenceBanksSub


class ClearanceSystemSub(supermod.ClearanceSystem):
    def __init__(self, clearanceSystemScheme='http://www.fpml.org/coding-scheme/clearance-system', valueOf_=None):
        super(ClearanceSystemSub, self).__init__(clearanceSystemScheme, valueOf_, )
supermod.ClearanceSystem.subclass = ClearanceSystemSub
# end class ClearanceSystemSub


class SwaptionPhysicalSettlementSub(supermod.SwaptionPhysicalSettlement):
    def __init__(self, clearedPhysicalSettlement=None, predeterminedClearingOrganizationPartyReference=None):
        super(SwaptionPhysicalSettlementSub, self).__init__(clearedPhysicalSettlement, predeterminedClearingOrganizationPartyReference, )
supermod.SwaptionPhysicalSettlement.subclass = SwaptionPhysicalSettlementSub
# end class SwaptionPhysicalSettlementSub


class CollateralSub(supermod.Collateral):
    def __init__(self, independentAmount=None):
        super(CollateralSub, self).__init__(independentAmount, )
supermod.Collateral.subclass = CollateralSub
# end class CollateralSub


class CollateralValueAllocationSub(supermod.CollateralValueAllocation):
    def __init__(self, type_=None, value=None):
        super(CollateralValueAllocationSub, self).__init__(type_, value, )
supermod.CollateralValueAllocation.subclass = CollateralValueAllocationSub
# end class CollateralValueAllocationSub


class ContactInformationSub(supermod.ContactInformation):
    def __init__(self, telephone=None, email=None, address=None):
        super(ContactInformationSub, self).__init__(telephone, email, address, )
supermod.ContactInformation.subclass = ContactInformationSub
# end class ContactInformationSub


class ContractualDefinitionsSub(supermod.ContractualDefinitions):
    def __init__(self, contractualDefinitionsScheme='http://www.fpml.org/coding-scheme/contractual-definitions', valueOf_=None):
        super(ContractualDefinitionsSub, self).__init__(contractualDefinitionsScheme, valueOf_, )
supermod.ContractualDefinitions.subclass = ContractualDefinitionsSub
# end class ContractualDefinitionsSub


class ContractualMatrixSub(supermod.ContractualMatrix):
    def __init__(self, matrixType=None, publicationDate=None, matrixTerm=None):
        super(ContractualMatrixSub, self).__init__(matrixType, publicationDate, matrixTerm, )
supermod.ContractualMatrix.subclass = ContractualMatrixSub
# end class ContractualMatrixSub


class ContractualSupplementSub(supermod.ContractualSupplement):
    def __init__(self, contractualSupplementScheme='http://www.fpml.org/coding-scheme/contractual-supplement', valueOf_=None):
        super(ContractualSupplementSub, self).__init__(contractualSupplementScheme, valueOf_, )
supermod.ContractualSupplement.subclass = ContractualSupplementSub
# end class ContractualSupplementSub


class ContractualTermsSupplementSub(supermod.ContractualTermsSupplement):
    def __init__(self, type_=None, publicationDate=None):
        super(ContractualTermsSupplementSub, self).__init__(type_, publicationDate, )
supermod.ContractualTermsSupplement.subclass = ContractualTermsSupplementSub
# end class ContractualTermsSupplementSub


class CorrespondentInformationSub(supermod.CorrespondentInformation):
    def __init__(self, routingIds=None, routingExplicitDetails=None, routingIdsAndExplicitDetails=None, correspondentPartyReference=None):
        super(CorrespondentInformationSub, self).__init__(routingIds, routingExplicitDetails, routingIdsAndExplicitDetails, correspondentPartyReference, )
supermod.CorrespondentInformation.subclass = CorrespondentInformationSub
# end class CorrespondentInformationSub


class CountryCodeSub(supermod.CountryCode):
    def __init__(self, countryScheme='http://www.fpml.org/coding-scheme/external/iso3166', valueOf_=None):
        super(CountryCodeSub, self).__init__(countryScheme, valueOf_, )
supermod.CountryCode.subclass = CountryCodeSub
# end class CountryCodeSub


class CreditSenioritySub(supermod.CreditSeniority):
    def __init__(self, creditSeniorityScheme='http://www.fpml.org/coding-scheme/credit-seniority', valueOf_=None):
        super(CreditSenioritySub, self).__init__(creditSeniorityScheme, valueOf_, )
supermod.CreditSeniority.subclass = CreditSenioritySub
# end class CreditSenioritySub


class CreditSupportAgreementSub(supermod.CreditSupportAgreement):
    def __init__(self, type_=None, date=None, identifier=None):
        super(CreditSupportAgreementSub, self).__init__(type_, date, identifier, )
supermod.CreditSupportAgreement.subclass = CreditSupportAgreementSub
# end class CreditSupportAgreementSub


class CreditSupportAgreementIdentifierSub(supermod.CreditSupportAgreementIdentifier):
    def __init__(self, creditSupportAgreementIdScheme=None, valueOf_=None):
        super(CreditSupportAgreementIdentifierSub, self).__init__(creditSupportAgreementIdScheme, valueOf_, )
supermod.CreditSupportAgreementIdentifier.subclass = CreditSupportAgreementIdentifierSub
# end class CreditSupportAgreementIdentifierSub


class CreditSupportAgreementTypeSub(supermod.CreditSupportAgreementType):
    def __init__(self, creditSupportAgreementTypeScheme='http://www.fpml.org/coding-scheme/credit-support-agreement-type', valueOf_=None):
        super(CreditSupportAgreementTypeSub, self).__init__(creditSupportAgreementTypeScheme, valueOf_, )
supermod.CreditSupportAgreementType.subclass = CreditSupportAgreementTypeSub
# end class CreditSupportAgreementTypeSub


class CreditRatingSub(supermod.CreditRating):
    def __init__(self, creditRatingScheme='http://www.fpml.org/coding-scheme/external/moodys', valueOf_=None):
        super(CreditRatingSub, self).__init__(creditRatingScheme, valueOf_, )
supermod.CreditRating.subclass = CreditRatingSub
# end class CreditRatingSub


class CurrencySub(supermod.Currency):
    def __init__(self, currencyScheme='http://www.fpml.org/coding-scheme/external/iso4217-2001-08-15', valueOf_=None, extensiontype_=None):
        super(CurrencySub, self).__init__(currencyScheme, valueOf_, extensiontype_, )
supermod.Currency.subclass = CurrencySub
# end class CurrencySub


class DateListSub(supermod.DateList):
    def __init__(self, date=None):
        super(DateListSub, self).__init__(date, )
supermod.DateList.subclass = DateListSub
# end class DateListSub


class DateRangeSub(supermod.DateRange):
    def __init__(self, unadjustedFirstDate=None, unadjustedLastDate=None, extensiontype_=None):
        super(DateRangeSub, self).__init__(unadjustedFirstDate, unadjustedLastDate, extensiontype_, )
supermod.DateRange.subclass = DateRangeSub
# end class DateRangeSub


class DateTimeListSub(supermod.DateTimeList):
    def __init__(self, dateTime=None):
        super(DateTimeListSub, self).__init__(dateTime, )
supermod.DateTimeList.subclass = DateTimeListSub
# end class DateTimeListSub


class DayCountFractionSub(supermod.DayCountFraction):
    def __init__(self, dayCountFractionScheme='http://www.fpml.org/coding-scheme/day-count-fraction', valueOf_=None):
        super(DayCountFractionSub, self).__init__(dayCountFractionScheme, valueOf_, )
supermod.DayCountFraction.subclass = DayCountFractionSub
# end class DayCountFractionSub


class DeterminationMethodSub(supermod.DeterminationMethod):
    def __init__(self, determinationMethodScheme='http://www.fpml.org/coding-scheme/determination-method', id=None, valueOf_=None):
        super(DeterminationMethodSub, self).__init__(determinationMethodScheme, id, valueOf_, )
supermod.DeterminationMethod.subclass = DeterminationMethodSub
# end class DeterminationMethodSub


class DocumentationSub(supermod.Documentation):
    def __init__(self, masterAgreement=None, masterConfirmation=None, brokerConfirmation=None, contractualDefinitions=None, contractualTermsSupplement=None, contractualMatrix=None, creditSupportAgreement=None, attachment=None):
        super(DocumentationSub, self).__init__(masterAgreement, masterConfirmation, brokerConfirmation, contractualDefinitions, contractualTermsSupplement, contractualMatrix, creditSupportAgreement, attachment, )
supermod.Documentation.subclass = DocumentationSub
# end class DocumentationSub


class EmbeddedOptionTypeSub(supermod.EmbeddedOptionType):
    def __init__(self, embeddedOptionTypeScheme='http://www.fpml.org/coding-scheme/embedded-option-type', valueOf_=None):
        super(EmbeddedOptionTypeSub, self).__init__(embeddedOptionTypeScheme, valueOf_, )
supermod.EmbeddedOptionType.subclass = EmbeddedOptionTypeSub
# end class EmbeddedOptionTypeSub


class EmptySub(supermod.Empty):
    def __init__(self):
        super(EmptySub, self).__init__()
supermod.Empty.subclass = EmptySub
# end class EmptySub


class EntityIdSub(supermod.EntityId):
    def __init__(self, entityIdScheme='http://www.fpml.org/coding-scheme/external/entity-id-RED-1-0', valueOf_=None):
        super(EntityIdSub, self).__init__(entityIdScheme, valueOf_, )
supermod.EntityId.subclass = EntityIdSub
# end class EntityIdSub


class EntityNameSub(supermod.EntityName):
    def __init__(self, entityNameScheme='http://www.fpml.org/coding-scheme/external/entity-name-RED-1-0', valueOf_=None):
        super(EntityNameSub, self).__init__(entityNameScheme, valueOf_, )
supermod.EntityName.subclass = EntityNameSub
# end class EntityNameSub


class ExchangeIdSub(supermod.ExchangeId):
    def __init__(self, exchangeIdScheme='http://www.fpml.org/coding-scheme/external/exchange-id-MIC-1-0', valueOf_=None):
        super(ExchangeIdSub, self).__init__(exchangeIdScheme, valueOf_, )
supermod.ExchangeId.subclass = ExchangeIdSub
# end class ExchangeIdSub


class ExerciseSub(supermod.Exercise):
    def __init__(self, id=None, extensiontype_=None):
        super(ExerciseSub, self).__init__(id, extensiontype_, )
supermod.Exercise.subclass = ExerciseSub
# end class ExerciseSub


class ExerciseFeeSub(supermod.ExerciseFee):
    def __init__(self, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, notionalReference=None, feeAmount=None, feeRate=None, feePaymentDate=None):
        super(ExerciseFeeSub, self).__init__(payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, notionalReference, feeAmount, feeRate, feePaymentDate, )
supermod.ExerciseFee.subclass = ExerciseFeeSub
# end class ExerciseFeeSub


class ExerciseFeeScheduleSub(supermod.ExerciseFeeSchedule):
    def __init__(self, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, notionalReference=None, feeAmountSchedule=None, feeRateSchedule=None, feePaymentDate=None):
        super(ExerciseFeeScheduleSub, self).__init__(payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, notionalReference, feeAmountSchedule, feeRateSchedule, feePaymentDate, )
supermod.ExerciseFeeSchedule.subclass = ExerciseFeeScheduleSub
# end class ExerciseFeeScheduleSub


class ExerciseNoticeSub(supermod.ExerciseNotice):
    def __init__(self, partyReference=None, exerciseNoticePartyReference=None, businessCenter=None):
        super(ExerciseNoticeSub, self).__init__(partyReference, exerciseNoticePartyReference, businessCenter, )
supermod.ExerciseNotice.subclass = ExerciseNoticeSub
# end class ExerciseNoticeSub


class ExerciseProcedureSub(supermod.ExerciseProcedure):
    def __init__(self, manualExercise=None, automaticExercise=None, followUpConfirmation=None, limitedRightToConfirm=None, splitTicket=None):
        super(ExerciseProcedureSub, self).__init__(manualExercise, automaticExercise, followUpConfirmation, limitedRightToConfirm, splitTicket, )
supermod.ExerciseProcedure.subclass = ExerciseProcedureSub
# end class ExerciseProcedureSub


class ExerciseProcedureOptionSub(supermod.ExerciseProcedureOption):
    def __init__(self, manualExercise=None, automaticExercise=None):
        super(ExerciseProcedureOptionSub, self).__init__(manualExercise, automaticExercise, )
supermod.ExerciseProcedureOption.subclass = ExerciseProcedureOptionSub
# end class ExerciseProcedureOptionSub


class FloatingRateIndexSub(supermod.FloatingRateIndex):
    def __init__(self, floatingRateIndexScheme='http://www.fpml.org/coding-scheme/floating-rate-index', valueOf_=None):
        super(FloatingRateIndexSub, self).__init__(floatingRateIndexScheme, valueOf_, )
supermod.FloatingRateIndex.subclass = FloatingRateIndexSub
# end class FloatingRateIndexSub


class ForecastRateIndexSub(supermod.ForecastRateIndex):
    def __init__(self, floatingRateIndex=None, indexTenor=None):
        super(ForecastRateIndexSub, self).__init__(floatingRateIndex, indexTenor, )
supermod.ForecastRateIndex.subclass = ForecastRateIndexSub
# end class ForecastRateIndexSub


class FormulaSub(supermod.Formula):
    def __init__(self, formulaDescription=None, math=None, formulaComponent=None):
        super(FormulaSub, self).__init__(formulaDescription, math, formulaComponent, )
supermod.Formula.subclass = FormulaSub
# end class FormulaSub


class FormulaComponentSub(supermod.FormulaComponent):
    def __init__(self, name=None, componentDescription=None, formula=None):
        super(FormulaComponentSub, self).__init__(name, componentDescription, formula, )
supermod.FormulaComponent.subclass = FormulaComponentSub
# end class FormulaComponentSub


class FrequencySub(supermod.Frequency):
    def __init__(self, id=None, periodMultiplier=None, period=None, extensiontype_=None):
        super(FrequencySub, self).__init__(id, periodMultiplier, period, extensiontype_, )
supermod.Frequency.subclass = FrequencySub
# end class FrequencySub


class FxCashSettlementSub(supermod.FxCashSettlement):
    def __init__(self, settlementCurrency=None, referenceCurrency=None, notionalAmount=None, fixing=None, rateSourceFixing=None, settlementDate=None):
        super(FxCashSettlementSub, self).__init__(settlementCurrency, referenceCurrency, notionalAmount, fixing, rateSourceFixing, settlementDate, )
supermod.FxCashSettlement.subclass = FxCashSettlementSub
# end class FxCashSettlementSub


class FxCashSettlementSimpleSub(supermod.FxCashSettlementSimple):
    def __init__(self, settlementCurrency=None, referenceCurrency=None, fixing=None, rateSourceFixing=None):
        super(FxCashSettlementSimpleSub, self).__init__(settlementCurrency, referenceCurrency, fixing, rateSourceFixing, )
supermod.FxCashSettlementSimple.subclass = FxCashSettlementSimpleSub
# end class FxCashSettlementSimpleSub


class FxFixingSub(supermod.FxFixing):
    def __init__(self, quotedCurrencyPair=None, fixingDate=None, fxSpotRateSource=None):
        super(FxFixingSub, self).__init__(quotedCurrencyPair, fixingDate, fxSpotRateSource, )
supermod.FxFixing.subclass = FxFixingSub
# end class FxFixingSub


class FxRateSub(supermod.FxRate):
    def __init__(self, quotedCurrencyPair=None, rate=None):
        super(FxRateSub, self).__init__(quotedCurrencyPair, rate, )
supermod.FxRate.subclass = FxRateSub
# end class FxRateSub


class FxRateSourceFixingSub(supermod.FxRateSourceFixing):
    def __init__(self, settlementRateSource=None, fixingDate=None):
        super(FxRateSourceFixingSub, self).__init__(settlementRateSource, fixingDate, )
supermod.FxRateSourceFixing.subclass = FxRateSourceFixingSub
# end class FxRateSourceFixingSub


class FxSettlementRateSourceSub(supermod.FxSettlementRateSource):
    def __init__(self, settlementRateOption=None, nonstandardSettlementRate=None):
        super(FxSettlementRateSourceSub, self).__init__(settlementRateOption, nonstandardSettlementRate, )
supermod.FxSettlementRateSource.subclass = FxSettlementRateSourceSub
# end class FxSettlementRateSourceSub


class FxSpotRateSourceSub(supermod.FxSpotRateSource):
    def __init__(self, primaryRateSource=None, secondaryRateSource=None, fixingTime=None):
        super(FxSpotRateSourceSub, self).__init__(primaryRateSource, secondaryRateSource, fixingTime, )
supermod.FxSpotRateSource.subclass = FxSpotRateSourceSub
# end class FxSpotRateSourceSub


class GenericAgreementSub(supermod.GenericAgreement):
    def __init__(self, type_=None, version=None, date=None, amendmentDate=None, governingLaw=None):
        super(GenericAgreementSub, self).__init__(type_, version, date, amendmentDate, governingLaw, )
supermod.GenericAgreement.subclass = GenericAgreementSub
# end class GenericAgreementSub


class GoverningLawSub(supermod.GoverningLaw):
    def __init__(self, governingLawScheme='http://www.fpml.org/coding-scheme/governing-law', valueOf_=None):
        super(GoverningLawSub, self).__init__(governingLawScheme, valueOf_, )
supermod.GoverningLaw.subclass = GoverningLawSub
# end class GoverningLawSub


class GrossCashflowSub(supermod.GrossCashflow):
    def __init__(self, cashflowId=None, partyTradeIdentifierReference=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, cashflowAmount=None, cashflowType=None):
        super(GrossCashflowSub, self).__init__(cashflowId, partyTradeIdentifierReference, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, cashflowAmount, cashflowType, )
supermod.GrossCashflow.subclass = GrossCashflowSub
# end class GrossCashflowSub


class IdentifiedCurrencySub(supermod.IdentifiedCurrency):
    def __init__(self, currencyScheme='http://www.fpml.org/coding-scheme/external/iso4217-2001-08-15', id=None, valueOf_=None):
        super(IdentifiedCurrencySub, self).__init__(currencyScheme, id, valueOf_, )
supermod.IdentifiedCurrency.subclass = IdentifiedCurrencySub
# end class IdentifiedCurrencySub


class IdentifiedDateSub(supermod.IdentifiedDate):
    def __init__(self, id=None, valueOf_=None):
        super(IdentifiedDateSub, self).__init__(id, valueOf_, )
supermod.IdentifiedDate.subclass = IdentifiedDateSub
# end class IdentifiedDateSub


class IdentifiedPayerReceiverSub(supermod.IdentifiedPayerReceiver):
    def __init__(self, id=None, valueOf_=None):
        super(IdentifiedPayerReceiverSub, self).__init__(id, valueOf_, )
supermod.IdentifiedPayerReceiver.subclass = IdentifiedPayerReceiverSub
# end class IdentifiedPayerReceiverSub


class IdentifiedRateSub(supermod.IdentifiedRate):
    def __init__(self, id=None, valueOf_=None):
        super(IdentifiedRateSub, self).__init__(id, valueOf_, )
supermod.IdentifiedRate.subclass = IdentifiedRateSub
# end class IdentifiedRateSub


class IndependentAmountSub(supermod.IndependentAmount):
    def __init__(self, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentDetail=None):
        super(IndependentAmountSub, self).__init__(payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentDetail, )
supermod.IndependentAmount.subclass = IndependentAmountSub
# end class IndependentAmountSub


class IndustryClassificationSub(supermod.IndustryClassification):
    def __init__(self, industryClassificationScheme='http://www.fpml.org/coding-scheme/regulatory-corporate-sector', valueOf_=None):
        super(IndustryClassificationSub, self).__init__(industryClassificationScheme, valueOf_, )
supermod.IndustryClassification.subclass = IndustryClassificationSub
# end class IndustryClassificationSub


class InformationProviderSub(supermod.InformationProvider):
    def __init__(self, informationProviderScheme='http://www.fpml.org/coding-scheme/information-provider', valueOf_=None):
        super(InformationProviderSub, self).__init__(informationProviderScheme, valueOf_, )
supermod.InformationProvider.subclass = InformationProviderSub
# end class InformationProviderSub


class InformationSourceSub(supermod.InformationSource):
    def __init__(self, rateSource=None, rateSourcePage=None, rateSourcePageHeading=None, extensiontype_=None):
        super(InformationSourceSub, self).__init__(rateSource, rateSourcePage, rateSourcePageHeading, extensiontype_, )
supermod.InformationSource.subclass = InformationSourceSub
# end class InformationSourceSub


class InstrumentIdSub(supermod.InstrumentId):
    def __init__(self, instrumentIdScheme=None, valueOf_=None):
        super(InstrumentIdSub, self).__init__(instrumentIdScheme, valueOf_, )
supermod.InstrumentId.subclass = InstrumentIdSub
# end class InstrumentIdSub


class InterestAccrualsMethodSub(supermod.InterestAccrualsMethod):
    def __init__(self, floatingRateCalculation=None, fixedRate=None, extensiontype_=None):
        super(InterestAccrualsMethodSub, self).__init__(floatingRateCalculation, fixedRate, extensiontype_, )
supermod.InterestAccrualsMethod.subclass = InterestAccrualsMethodSub
# end class InterestAccrualsMethodSub


class IntermediaryInformationSub(supermod.IntermediaryInformation):
    def __init__(self, routingIds=None, routingExplicitDetails=None, routingIdsAndExplicitDetails=None, intermediarySequenceNumber=None, intermediaryPartyReference=None):
        super(IntermediaryInformationSub, self).__init__(routingIds, routingExplicitDetails, routingIdsAndExplicitDetails, intermediarySequenceNumber, intermediaryPartyReference, )
supermod.IntermediaryInformation.subclass = IntermediaryInformationSub
# end class IntermediaryInformationSub


class InterpolationMethodSub(supermod.InterpolationMethod):
    def __init__(self, interpolationMethodScheme='http://www.fpml.org/coding-scheme/interpolation-method', valueOf_=None):
        super(InterpolationMethodSub, self).__init__(interpolationMethodScheme, valueOf_, )
supermod.InterpolationMethod.subclass = InterpolationMethodSub
# end class InterpolationMethodSub


class LanguageSub(supermod.Language):
    def __init__(self, languageScheme=None, valueOf_=None):
        super(LanguageSub, self).__init__(languageScheme, valueOf_, )
supermod.Language.subclass = LanguageSub
# end class LanguageSub


class LegSub(supermod.Leg):
    def __init__(self, id=None, extensiontype_=None):
        super(LegSub, self).__init__(id, extensiontype_, )
supermod.Leg.subclass = LegSub
# end class LegSub


class LegIdSub(supermod.LegId):
    def __init__(self, legIdScheme=None, valueOf_=None):
        super(LegIdSub, self).__init__(legIdScheme, valueOf_, )
supermod.LegId.subclass = LegIdSub
# end class LegIdSub


class LegIdentifierSub(supermod.LegIdentifier):
    def __init__(self, legId=None, version=None, effectiveDate=None):
        super(LegIdentifierSub, self).__init__(legId, version, effectiveDate, )
supermod.LegIdentifier.subclass = LegIdentifierSub
# end class LegIdentifierSub


class LegalEntitySub(supermod.LegalEntity):
    def __init__(self, id=None, entityName=None, entityId=None):
        super(LegalEntitySub, self).__init__(id, entityName, entityId, )
supermod.LegalEntity.subclass = LegalEntitySub
# end class LegalEntitySub


class MainPublicationSub(supermod.MainPublication):
    def __init__(self, mainPublicationScheme='http://www.fpml.org/coding-scheme/inflation-main-publication', valueOf_=None):
        super(MainPublicationSub, self).__init__(mainPublicationScheme, valueOf_, )
supermod.MainPublication.subclass = MainPublicationSub
# end class MainPublicationSub


class ManualExerciseSub(supermod.ManualExercise):
    def __init__(self, exerciseNotice=None, fallbackExercise=None):
        super(ManualExerciseSub, self).__init__(exerciseNotice, fallbackExercise, )
supermod.ManualExercise.subclass = ManualExerciseSub
# end class ManualExerciseSub


class MasterAgreementSub(supermod.MasterAgreement):
    def __init__(self, masterAgreementId=None, masterAgreementType=None, masterAgreementVersion=None, masterAgreementDate=None):
        super(MasterAgreementSub, self).__init__(masterAgreementId, masterAgreementType, masterAgreementVersion, masterAgreementDate, )
supermod.MasterAgreement.subclass = MasterAgreementSub
# end class MasterAgreementSub


class MasterAgreementIdSub(supermod.MasterAgreementId):
    def __init__(self, masterAgreementIdScheme=None, valueOf_=None):
        super(MasterAgreementIdSub, self).__init__(masterAgreementIdScheme, valueOf_, )
supermod.MasterAgreementId.subclass = MasterAgreementIdSub
# end class MasterAgreementIdSub


class MasterAgreementTypeSub(supermod.MasterAgreementType):
    def __init__(self, masterAgreementTypeScheme='http://www.fpml.org/coding-scheme/master-agreement-type', valueOf_=None):
        super(MasterAgreementTypeSub, self).__init__(masterAgreementTypeScheme, valueOf_, )
supermod.MasterAgreementType.subclass = MasterAgreementTypeSub
# end class MasterAgreementTypeSub


class MasterAgreementVersionSub(supermod.MasterAgreementVersion):
    def __init__(self, masterAgreementVersionScheme='http://www.fpml.org/coding-scheme/master-agreement-version', valueOf_=None):
        super(MasterAgreementVersionSub, self).__init__(masterAgreementVersionScheme, valueOf_, )
supermod.MasterAgreementVersion.subclass = MasterAgreementVersionSub
# end class MasterAgreementVersionSub


class MasterConfirmationSub(supermod.MasterConfirmation):
    def __init__(self, masterConfirmationType=None, masterConfirmationDate=None, masterConfirmationAnnexDate=None, masterConfirmationAnnexType=None):
        super(MasterConfirmationSub, self).__init__(masterConfirmationType, masterConfirmationDate, masterConfirmationAnnexDate, masterConfirmationAnnexType, )
supermod.MasterConfirmation.subclass = MasterConfirmationSub
# end class MasterConfirmationSub


class MasterConfirmationAnnexTypeSub(supermod.MasterConfirmationAnnexType):
    def __init__(self, masterConfirmationAnnexTypeScheme='http://www.fpml.org/coding-scheme/master-confirmation-annex-type', valueOf_=None):
        super(MasterConfirmationAnnexTypeSub, self).__init__(masterConfirmationAnnexTypeScheme, valueOf_, )
supermod.MasterConfirmationAnnexType.subclass = MasterConfirmationAnnexTypeSub
# end class MasterConfirmationAnnexTypeSub


class MasterConfirmationTypeSub(supermod.MasterConfirmationType):
    def __init__(self, masterConfirmationTypeScheme='http://www.fpml.org/coding-scheme/master-confirmation-type', valueOf_=None):
        super(MasterConfirmationTypeSub, self).__init__(masterConfirmationTypeScheme, valueOf_, )
supermod.MasterConfirmationType.subclass = MasterConfirmationTypeSub
# end class MasterConfirmationTypeSub


class MatchIdSub(supermod.MatchId):
    def __init__(self, matchIdScheme=None, valueOf_=None):
        super(MatchIdSub, self).__init__(matchIdScheme, valueOf_, )
supermod.MatchId.subclass = MatchIdSub
# end class MatchIdSub


class MathSub(supermod.Math):
    def __init__(self, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(MathSub, self).__init__(anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.Math.subclass = MathSub
# end class MathSub


class MatrixTypeSub(supermod.MatrixType):
    def __init__(self, matrixTypeScheme='http://www.fpml.org/coding-scheme/matrix-type', valueOf_=None):
        super(MatrixTypeSub, self).__init__(matrixTypeScheme, valueOf_, )
supermod.MatrixType.subclass = MatrixTypeSub
# end class MatrixTypeSub


class MatrixTermSub(supermod.MatrixTerm):
    def __init__(self, matrixTermScheme='http://www.fpml.org/coding-scheme/credit-matrix-transaction-type', valueOf_=None):
        super(MatrixTermSub, self).__init__(matrixTermScheme, valueOf_, )
supermod.MatrixTerm.subclass = MatrixTermSub
# end class MatrixTermSub


class MimeTypeSub(supermod.MimeType):
    def __init__(self, mimeTypeScheme=None, valueOf_=None):
        super(MimeTypeSub, self).__init__(mimeTypeScheme, valueOf_, )
supermod.MimeType.subclass = MimeTypeSub
# end class MimeTypeSub


class MoneyBaseSub(supermod.MoneyBase):
    def __init__(self, id=None, currency=None, extensiontype_=None):
        super(MoneyBaseSub, self).__init__(id, currency, extensiontype_, )
supermod.MoneyBase.subclass = MoneyBaseSub
# end class MoneyBaseSub


class MultipleExerciseSub(supermod.MultipleExercise):
    def __init__(self, notionalReference=None, integralMultipleAmount=None, minimumNotionalAmount=None, minimumNumberOfOptions=None, maximumNotionalAmount=None, maximumNumberOfOptions=None):
        super(MultipleExerciseSub, self).__init__(notionalReference, integralMultipleAmount, minimumNotionalAmount, minimumNumberOfOptions, maximumNotionalAmount, maximumNumberOfOptions, )
supermod.MultipleExercise.subclass = MultipleExerciseSub
# end class MultipleExerciseSub


class NonNegativeMoneySub(supermod.NonNegativeMoney):
    def __init__(self, id=None, currency=None, amount=None, extensiontype_=None):
        super(NonNegativeMoneySub, self).__init__(id, currency, amount, extensiontype_, )
supermod.NonNegativeMoney.subclass = NonNegativeMoneySub
# end class NonNegativeMoneySub


class NonNegativeScheduleSub(supermod.NonNegativeSchedule):
    def __init__(self, id=None, initialValue=None, step=None, extensiontype_=None):
        super(NonNegativeScheduleSub, self).__init__(id, initialValue, step, extensiontype_, )
supermod.NonNegativeSchedule.subclass = NonNegativeScheduleSub
# end class NonNegativeScheduleSub


class NotionalAmountSub(supermod.NotionalAmount):
    def __init__(self, id=None, currency=None, amount=None):
        super(NotionalAmountSub, self).__init__(id, currency, amount, )
supermod.NotionalAmount.subclass = NotionalAmountSub
# end class NotionalAmountSub


class OffsetPrevailingTimeSub(supermod.OffsetPrevailingTime):
    def __init__(self, time=None, offset=None):
        super(OffsetPrevailingTimeSub, self).__init__(time, offset, )
supermod.OffsetPrevailingTime.subclass = OffsetPrevailingTimeSub
# end class OffsetPrevailingTimeSub


class OnBehalfOfSub(supermod.OnBehalfOf):
    def __init__(self, partyReference=None, accountReference=None):
        super(OnBehalfOfSub, self).__init__(partyReference, accountReference, )
supermod.OnBehalfOf.subclass = OnBehalfOfSub
# end class OnBehalfOfSub


class OrganizationTypeSub(supermod.OrganizationType):
    def __init__(self, organizationTypeScheme='http://www.fpml.org/coding-scheme/organization-type', valueOf_=None):
        super(OrganizationTypeSub, self).__init__(organizationTypeScheme, valueOf_, )
supermod.OrganizationType.subclass = OrganizationTypeSub
# end class OrganizationTypeSub


class OriginatingEventSub(supermod.OriginatingEvent):
    def __init__(self, originatingEventScheme='http://www.fpml.org/coding-scheme/originating-event', valueOf_=None):
        super(OriginatingEventSub, self).__init__(originatingEventScheme, valueOf_, )
supermod.OriginatingEvent.subclass = OriginatingEventSub
# end class OriginatingEventSub


class PartialExerciseSub(supermod.PartialExercise):
    def __init__(self, notionalReference=None, integralMultipleAmount=None, minimumNotionalAmount=None, minimumNumberOfOptions=None):
        super(PartialExerciseSub, self).__init__(notionalReference, integralMultipleAmount, minimumNotionalAmount, minimumNumberOfOptions, )
supermod.PartialExercise.subclass = PartialExerciseSub
# end class PartialExerciseSub


class PartySub(supermod.Party):
    def __init__(self, id=None, partyId=None, partyName=None, classification=None, creditRating=None, country=None, region=None, jurisdiction=None, organizationType=None, relatedParty=None, contactInfo=None, businessUnit=None, person=None, groupType=None, partyReference=None):
        super(PartySub, self).__init__(id, partyId, partyName, classification, creditRating, country, region, jurisdiction, organizationType, relatedParty, contactInfo, businessUnit, person, groupType, partyReference, )
supermod.Party.subclass = PartySub
# end class PartySub


class PartyContactInformationSub(supermod.PartyContactInformation):
    def __init__(self, partyReference=None, contactInfo=None, businessUnit=None, person=None):
        super(PartyContactInformationSub, self).__init__(partyReference, contactInfo, businessUnit, person, )
supermod.PartyContactInformation.subclass = PartyContactInformationSub
# end class PartyContactInformationSub


class PartyGroupTypeSub(supermod.PartyGroupType):
    def __init__(self, partyGroupTypeScheme='http://www.fpml.org/coding-scheme/party-group-type', valueOf_=None):
        super(PartyGroupTypeSub, self).__init__(partyGroupTypeScheme, valueOf_, )
supermod.PartyGroupType.subclass = PartyGroupTypeSub
# end class PartyGroupTypeSub


class PartyIdSub(supermod.PartyId):
    def __init__(self, partyIdScheme='http://www.fpml.org/coding-scheme/external/iso9362', valueOf_=None):
        super(PartyIdSub, self).__init__(partyIdScheme, valueOf_, )
supermod.PartyId.subclass = PartyIdSub
# end class PartyIdSub


class PartyNameSub(supermod.PartyName):
    def __init__(self, partyNameScheme=None, valueOf_=None):
        super(PartyNameSub, self).__init__(partyNameScheme, valueOf_, )
supermod.PartyName.subclass = PartyNameSub
# end class PartyNameSub


class PartyRelationshipSub(supermod.PartyRelationship):
    def __init__(self, partyReference=None, accountReference=None, role=None, type_=None, effectiveDate=None, terminationDate=None, documentation=None):
        super(PartyRelationshipSub, self).__init__(partyReference, accountReference, role, type_, effectiveDate, terminationDate, documentation, )
supermod.PartyRelationship.subclass = PartyRelationshipSub
# end class PartyRelationshipSub


class PartyRelationshipDocumentationSub(supermod.PartyRelationshipDocumentation):
    def __init__(self, masterAgreement=None, creditSupportAgreement=None, agreement=None):
        super(PartyRelationshipDocumentationSub, self).__init__(masterAgreement, creditSupportAgreement, agreement, )
supermod.PartyRelationshipDocumentation.subclass = PartyRelationshipDocumentationSub
# end class PartyRelationshipDocumentationSub


class PartyRoleSub(supermod.PartyRole):
    def __init__(self, partyRoleScheme='http://www.fpml.org/coding-scheme/party-role', valueOf_=None):
        super(PartyRoleSub, self).__init__(partyRoleScheme, valueOf_, )
supermod.PartyRole.subclass = PartyRoleSub
# end class PartyRoleSub


class PartyRoleTypeSub(supermod.PartyRoleType):
    def __init__(self, partyRoleTypeScheme='http://www.fpml.org/coding-scheme/party-role-type', valueOf_=None):
        super(PartyRoleTypeSub, self).__init__(partyRoleTypeScheme, valueOf_, )
supermod.PartyRoleType.subclass = PartyRoleTypeSub
# end class PartyRoleTypeSub


class PaymentBaseSub(supermod.PaymentBase):
    def __init__(self, id=None, extensiontype_=None):
        super(PaymentBaseSub, self).__init__(id, extensiontype_, )
supermod.PaymentBase.subclass = PaymentBaseSub
# end class PaymentBaseSub


class PaymentBaseExtendedSub(supermod.PaymentBaseExtended):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentDate=None, extensiontype_=None):
        super(PaymentBaseExtendedSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentDate, extensiontype_, )
supermod.PaymentBaseExtended.subclass = PaymentBaseExtendedSub
# end class PaymentBaseExtendedSub


class PaymentDetailSub(supermod.PaymentDetail):
    def __init__(self, id=None, paymentDate=None, paymentAmount=None, paymentRule=None):
        super(PaymentDetailSub, self).__init__(id, paymentDate, paymentAmount, paymentRule, )
supermod.PaymentDetail.subclass = PaymentDetailSub
# end class PaymentDetailSub


class PaymentDetailsSub(supermod.PaymentDetails):
    def __init__(self, paymentReference=None, grossCashflow=None, settlementInformation=None):
        super(PaymentDetailsSub, self).__init__(paymentReference, grossCashflow, settlementInformation, )
supermod.PaymentDetails.subclass = PaymentDetailsSub
# end class PaymentDetailsSub


class PaymentIdSub(supermod.PaymentId):
    def __init__(self, paymentIdScheme=None, valueOf_=None):
        super(PaymentIdSub, self).__init__(paymentIdScheme, valueOf_, )
supermod.PaymentId.subclass = PaymentIdSub
# end class PaymentIdSub


class PaymentRuleSub(supermod.PaymentRule):
    def __init__(self):
        super(PaymentRuleSub, self).__init__()
supermod.PaymentRule.subclass = PaymentRuleSub
# end class PaymentRuleSub


class PaymentTypeSub(supermod.PaymentType):
    def __init__(self, paymentTypeScheme=None, valueOf_=None):
        super(PaymentTypeSub, self).__init__(paymentTypeScheme, valueOf_, )
supermod.PaymentType.subclass = PaymentTypeSub
# end class PaymentTypeSub


class PeriodSub(supermod.Period):
    def __init__(self, id=None, periodMultiplier=None, period=None, extensiontype_=None):
        super(PeriodSub, self).__init__(id, periodMultiplier, period, extensiontype_, )
supermod.Period.subclass = PeriodSub
# end class PeriodSub


class PeriodicDatesSub(supermod.PeriodicDates):
    def __init__(self, calculationStartDate=None, calculationEndDate=None, calculationPeriodFrequency=None, calculationPeriodDatesAdjustments=None):
        super(PeriodicDatesSub, self).__init__(calculationStartDate, calculationEndDate, calculationPeriodFrequency, calculationPeriodDatesAdjustments, )
supermod.PeriodicDates.subclass = PeriodicDatesSub
# end class PeriodicDatesSub


class PersonSub(supermod.Person):
    def __init__(self, id=None, honorific=None, firstName=None, middleName=None, initial=None, surname=None, suffix=None, personId=None, businessUnitReference=None, contactInfo=None, dateOfBirth=None, country=None):
        super(PersonSub, self).__init__(id, honorific, firstName, middleName, initial, surname, suffix, personId, businessUnitReference, contactInfo, dateOfBirth, country, )
supermod.Person.subclass = PersonSub
# end class PersonSub


class PersonIdSub(supermod.PersonId):
    def __init__(self, personIdScheme=None, valueOf_=None):
        super(PersonIdSub, self).__init__(personIdScheme, valueOf_, )
supermod.PersonId.subclass = PersonIdSub
# end class PersonIdSub


class PersonRoleSub(supermod.PersonRole):
    def __init__(self, personRoleScheme='http://www.fpml.org/coding-scheme/person-role', valueOf_=None):
        super(PersonRoleSub, self).__init__(personRoleScheme, valueOf_, )
supermod.PersonRole.subclass = PersonRoleSub
# end class PersonRoleSub


class PositiveMoneySub(supermod.PositiveMoney):
    def __init__(self, id=None, currency=None, amount=None):
        super(PositiveMoneySub, self).__init__(id, currency, amount, )
supermod.PositiveMoney.subclass = PositiveMoneySub
# end class PositiveMoneySub


class PrevailingTimeSub(supermod.PrevailingTime):
    def __init__(self, hourMinuteTime=None, location=None):
        super(PrevailingTimeSub, self).__init__(hourMinuteTime, location, )
supermod.PrevailingTime.subclass = PrevailingTimeSub
# end class PrevailingTimeSub


class PricingStructureSub(supermod.PricingStructure):
    def __init__(self, id=None, name=None, currency=None):
        super(PricingStructureSub, self).__init__(id, name, currency, )
supermod.PricingStructure.subclass = PricingStructureSub
# end class PricingStructureSub


class PrincipalExchangesSub(supermod.PrincipalExchanges):
    def __init__(self, id=None, initialExchange=None, finalExchange=None, intermediateExchange=None):
        super(PrincipalExchangesSub, self).__init__(id, initialExchange, finalExchange, intermediateExchange, )
supermod.PrincipalExchanges.subclass = PrincipalExchangesSub
# end class PrincipalExchangesSub


class ProductSub(supermod.Product):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, extensiontype_=None):
        super(ProductSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, extensiontype_, )
supermod.Product.subclass = ProductSub
# end class ProductSub


class ProductIdSub(supermod.ProductId):
    def __init__(self, productIdScheme=None, valueOf_=None):
        super(ProductIdSub, self).__init__(productIdScheme, valueOf_, )
supermod.ProductId.subclass = ProductIdSub
# end class ProductIdSub


class ProductTypeSub(supermod.ProductType):
    def __init__(self, productTypeScheme='http://www.fpml.org/coding-scheme/product-taxonomy', valueOf_=None):
        super(ProductTypeSub, self).__init__(productTypeScheme, valueOf_, )
supermod.ProductType.subclass = ProductTypeSub
# end class ProductTypeSub


class ProposedCollateralAllocationSub(supermod.ProposedCollateralAllocation):
    def __init__(self, allocationPartyReference=None, allocationAccountReference=None, collateralValueAllocation=None):
        super(ProposedCollateralAllocationSub, self).__init__(allocationPartyReference, allocationAccountReference, collateralValueAllocation, )
supermod.ProposedCollateralAllocation.subclass = ProposedCollateralAllocationSub
# end class ProposedCollateralAllocationSub


class QuotedCurrencyPairSub(supermod.QuotedCurrencyPair):
    def __init__(self, currency1=None, currency2=None, quoteBasis=None, extensiontype_=None):
        super(QuotedCurrencyPairSub, self).__init__(currency1, currency2, quoteBasis, extensiontype_, )
supermod.QuotedCurrencyPair.subclass = QuotedCurrencyPairSub
# end class QuotedCurrencyPairSub


class RateSub(supermod.Rate):
    def __init__(self, id=None, extensiontype_=None):
        super(RateSub, self).__init__(id, extensiontype_, )
supermod.Rate.subclass = RateSub
# end class RateSub


class RateObservationSub(supermod.RateObservation):
    def __init__(self, id=None, resetDate=None, adjustedFixingDate=None, observedRate=None, treatedRate=None, observationWeight=None, rateReference=None, forecastRate=None, treatedForecastRate=None):
        super(RateObservationSub, self).__init__(id, resetDate, adjustedFixingDate, observedRate, treatedRate, observationWeight, rateReference, forecastRate, treatedForecastRate, )
supermod.RateObservation.subclass = RateObservationSub
# end class RateObservationSub


class RateReferenceSub(supermod.RateReference):
    def __init__(self, href=None):
        super(RateReferenceSub, self).__init__(href, )
supermod.RateReference.subclass = RateReferenceSub
# end class RateReferenceSub


class RateSourcePageSub(supermod.RateSourcePage):
    def __init__(self, rateSourcePageScheme=None, valueOf_=None):
        super(RateSourcePageSub, self).__init__(rateSourcePageScheme, valueOf_, )
supermod.RateSourcePage.subclass = RateSourcePageSub
# end class RateSourcePageSub


class ReferenceSub(supermod.Reference):
    def __init__(self, extensiontype_=None):
        super(ReferenceSub, self).__init__(extensiontype_, )
supermod.Reference.subclass = ReferenceSub
# end class ReferenceSub


class ReferenceAmountSub(supermod.ReferenceAmount):
    def __init__(self, referenceAmountScheme=None, valueOf_=None):
        super(ReferenceAmountSub, self).__init__(referenceAmountScheme, valueOf_, )
supermod.ReferenceAmount.subclass = ReferenceAmountSub
# end class ReferenceAmountSub


class ReferenceBankSub(supermod.ReferenceBank):
    def __init__(self, referenceBankId=None, referenceBankName=None):
        super(ReferenceBankSub, self).__init__(referenceBankId, referenceBankName, )
supermod.ReferenceBank.subclass = ReferenceBankSub
# end class ReferenceBankSub


class ReferenceBankIdSub(supermod.ReferenceBankId):
    def __init__(self, referenceBankIdScheme=None, valueOf_=None):
        super(ReferenceBankIdSub, self).__init__(referenceBankIdScheme, valueOf_, )
supermod.ReferenceBankId.subclass = ReferenceBankIdSub
# end class ReferenceBankIdSub


class RegionSub(supermod.Region):
    def __init__(self, regionScheme='http://www.fpml.org/coding-scheme/region', valueOf_=None):
        super(RegionSub, self).__init__(regionScheme, valueOf_, )
supermod.Region.subclass = RegionSub
# end class RegionSub


class RelatedBusinessUnitSub(supermod.RelatedBusinessUnit):
    def __init__(self, businessUnitReference=None, role=None):
        super(RelatedBusinessUnitSub, self).__init__(businessUnitReference, role, )
supermod.RelatedBusinessUnit.subclass = RelatedBusinessUnitSub
# end class RelatedBusinessUnitSub


class RelatedPartySub(supermod.RelatedParty):
    def __init__(self, partyReference=None, accountReference=None, role=None, type_=None):
        super(RelatedPartySub, self).__init__(partyReference, accountReference, role, type_, )
supermod.RelatedParty.subclass = RelatedPartySub
# end class RelatedPartySub


class RelatedPersonSub(supermod.RelatedPerson):
    def __init__(self, personReference=None, role=None):
        super(RelatedPersonSub, self).__init__(personReference, role, )
supermod.RelatedPerson.subclass = RelatedPersonSub
# end class RelatedPersonSub


class RelativeDateSequenceSub(supermod.RelativeDateSequence):
    def __init__(self, dateRelativeTo=None, dateOffset=None, businessCentersReference=None, businessCenters=None):
        super(RelativeDateSequenceSub, self).__init__(dateRelativeTo, dateOffset, businessCentersReference, businessCenters, )
supermod.RelativeDateSequence.subclass = RelativeDateSequenceSub
# end class RelativeDateSequenceSub


class ReportingRegimeNameSub(supermod.ReportingRegimeName):
    def __init__(self, reportingRegimeNameScheme='http://www.fpml.org/coding-scheme/reporting-regime', valueOf_=None):
        super(ReportingRegimeNameSub, self).__init__(reportingRegimeNameScheme, valueOf_, )
supermod.ReportingRegimeName.subclass = ReportingRegimeNameSub
# end class ReportingRegimeNameSub


class RequestedActionSub(supermod.RequestedAction):
    def __init__(self, requestedActionScheme='http://www.fpml.org/coding-scheme/requested-action', valueOf_=None):
        super(RequestedActionSub, self).__init__(requestedActionScheme, valueOf_, )
supermod.RequestedAction.subclass = RequestedActionSub
# end class RequestedActionSub


class RequiredIdentifierDateSub(supermod.RequiredIdentifierDate):
    def __init__(self, id=None, valueOf_=None):
        super(RequiredIdentifierDateSub, self).__init__(id, valueOf_, )
supermod.RequiredIdentifierDate.subclass = RequiredIdentifierDateSub
# end class RequiredIdentifierDateSub


class ResetFrequencySub(supermod.ResetFrequency):
    def __init__(self, id=None, periodMultiplier=None, period=None, weeklyRollConvention=None):
        super(ResetFrequencySub, self).__init__(id, periodMultiplier, period, weeklyRollConvention, )
supermod.ResetFrequency.subclass = ResetFrequencySub
# end class ResetFrequencySub


class ResourceSub(supermod.Resource):
    def __init__(self, resourceId=None, resourceType=None, language=None, sizeInBytes=None, length=None, mimeType=None, name=None, comments=None, string=None, hexadecimalBinary=None, base64Binary=None, url=None):
        super(ResourceSub, self).__init__(resourceId, resourceType, language, sizeInBytes, length, mimeType, name, comments, string, hexadecimalBinary, base64Binary, url, )
supermod.Resource.subclass = ResourceSub
# end class ResourceSub


class ResourceIdSub(supermod.ResourceId):
    def __init__(self, resourceIdScheme=None, valueOf_=None):
        super(ResourceIdSub, self).__init__(resourceIdScheme, valueOf_, )
supermod.ResourceId.subclass = ResourceIdSub
# end class ResourceIdSub


class ResourceLengthSub(supermod.ResourceLength):
    def __init__(self, lengthUnit=None, lengthValue=None):
        super(ResourceLengthSub, self).__init__(lengthUnit, lengthValue, )
supermod.ResourceLength.subclass = ResourceLengthSub
# end class ResourceLengthSub


class ResourceTypeSub(supermod.ResourceType):
    def __init__(self, resourceTypeScheme='http://www.fpml.org/coding-scheme/resource-type', valueOf_=None):
        super(ResourceTypeSub, self).__init__(resourceTypeScheme, valueOf_, )
supermod.ResourceType.subclass = ResourceTypeSub
# end class ResourceTypeSub


class ReturnSwapNotionalAmountReferenceSub(supermod.ReturnSwapNotionalAmountReference):
    def __init__(self, href=None):
        super(ReturnSwapNotionalAmountReferenceSub, self).__init__(href, )
supermod.ReturnSwapNotionalAmountReference.subclass = ReturnSwapNotionalAmountReferenceSub
# end class ReturnSwapNotionalAmountReferenceSub


class RoundingSub(supermod.Rounding):
    def __init__(self, roundingDirection=None, precision=None):
        super(RoundingSub, self).__init__(roundingDirection, precision, )
supermod.Rounding.subclass = RoundingSub
# end class RoundingSub


class RoutingSub(supermod.Routing):
    def __init__(self, routingIds=None, routingExplicitDetails=None, routingIdsAndExplicitDetails=None):
        super(RoutingSub, self).__init__(routingIds, routingExplicitDetails, routingIdsAndExplicitDetails, )
supermod.Routing.subclass = RoutingSub
# end class RoutingSub


class RoutingExplicitDetailsSub(supermod.RoutingExplicitDetails):
    def __init__(self, routingName=None, routingAddress=None, routingAccountNumber=None, routingReferenceText=None):
        super(RoutingExplicitDetailsSub, self).__init__(routingName, routingAddress, routingAccountNumber, routingReferenceText, )
supermod.RoutingExplicitDetails.subclass = RoutingExplicitDetailsSub
# end class RoutingExplicitDetailsSub


class RoutingIdSub(supermod.RoutingId):
    def __init__(self, routingIdCodeScheme='http://www.fpml.org/coding-scheme/external/iso9362', valueOf_=None):
        super(RoutingIdSub, self).__init__(routingIdCodeScheme, valueOf_, )
supermod.RoutingId.subclass = RoutingIdSub
# end class RoutingIdSub


class RoutingIdsSub(supermod.RoutingIds):
    def __init__(self, routingId=None):
        super(RoutingIdsSub, self).__init__(routingId, )
supermod.RoutingIds.subclass = RoutingIdsSub
# end class RoutingIdsSub


class RoutingIdsAndExplicitDetailsSub(supermod.RoutingIdsAndExplicitDetails):
    def __init__(self, routingIds=None, routingName=None, routingAddress=None, routingAccountNumber=None, routingReferenceText=None):
        super(RoutingIdsAndExplicitDetailsSub, self).__init__(routingIds, routingName, routingAddress, routingAccountNumber, routingReferenceText, )
supermod.RoutingIdsAndExplicitDetails.subclass = RoutingIdsAndExplicitDetailsSub
# end class RoutingIdsAndExplicitDetailsSub


class ScheduleSub(supermod.Schedule):
    def __init__(self, id=None, initialValue=None, step=None, extensiontype_=None):
        super(ScheduleSub, self).__init__(id, initialValue, step, extensiontype_, )
supermod.Schedule.subclass = ScheduleSub
# end class ScheduleSub


class ScheduleReferenceSub(supermod.ScheduleReference):
    def __init__(self, href=None):
        super(ScheduleReferenceSub, self).__init__(href, )
supermod.ScheduleReference.subclass = ScheduleReferenceSub
# end class ScheduleReferenceSub


class SettlementInformationSub(supermod.SettlementInformation):
    def __init__(self, standardSettlementStyle=None, settlementInstruction=None):
        super(SettlementInformationSub, self).__init__(standardSettlementStyle, settlementInstruction, )
supermod.SettlementInformation.subclass = SettlementInformationSub
# end class SettlementInformationSub


class SettlementInstructionSub(supermod.SettlementInstruction):
    def __init__(self, settlementMethod=None, correspondentInformation=None, intermediaryInformation=None, beneficiaryBank=None, beneficiary=None, depositoryPartyReference=None, splitSettlement=None):
        super(SettlementInstructionSub, self).__init__(settlementMethod, correspondentInformation, intermediaryInformation, beneficiaryBank, beneficiary, depositoryPartyReference, splitSettlement, )
supermod.SettlementInstruction.subclass = SettlementInstructionSub
# end class SettlementInstructionSub


class SettlementMethodSub(supermod.SettlementMethod):
    def __init__(self, settlementMethodScheme='http://www.fpml.org/coding-scheme/settlement-method', valueOf_=None):
        super(SettlementMethodSub, self).__init__(settlementMethodScheme, valueOf_, )
supermod.SettlementMethod.subclass = SettlementMethodSub
# end class SettlementMethodSub


class SettlementPriceDefaultElectionSub(supermod.SettlementPriceDefaultElection):
    def __init__(self, settlementPriceDefaultElectionScheme='http://www.fpml.org/coding-scheme/settlement-price-default-election', valueOf_=None):
        super(SettlementPriceDefaultElectionSub, self).__init__(settlementPriceDefaultElectionScheme, valueOf_, )
supermod.SettlementPriceDefaultElection.subclass = SettlementPriceDefaultElectionSub
# end class SettlementPriceDefaultElectionSub


class SettlementPriceSourceSub(supermod.SettlementPriceSource):
    def __init__(self, settlementPriceSourceScheme='http://www.fpml.org/coding-scheme/settlement-price-source', valueOf_=None):
        super(SettlementPriceSourceSub, self).__init__(settlementPriceSourceScheme, valueOf_, )
supermod.SettlementPriceSource.subclass = SettlementPriceSourceSub
# end class SettlementPriceSourceSub


class SettlementRateOptionSub(supermod.SettlementRateOption):
    def __init__(self, settlementRateOptionScheme='http://www.fpml.org/coding-scheme/settlement-rate-option', valueOf_=None):
        super(SettlementRateOptionSub, self).__init__(settlementRateOptionScheme, valueOf_, )
supermod.SettlementRateOption.subclass = SettlementRateOptionSub
# end class SettlementRateOptionSub


class SettlementRateSourceSub(supermod.SettlementRateSource):
    def __init__(self, informationSource=None, cashSettlementReferenceBanks=None):
        super(SettlementRateSourceSub, self).__init__(informationSource, cashSettlementReferenceBanks, )
supermod.SettlementRateSource.subclass = SettlementRateSourceSub
# end class SettlementRateSourceSub


class SharedAmericanExerciseSub(supermod.SharedAmericanExercise):
    def __init__(self, id=None, commencementDate=None, expirationDate=None, latestExerciseTime=None, latestExerciseTimeDetermination=None):
        super(SharedAmericanExerciseSub, self).__init__(id, commencementDate, expirationDate, latestExerciseTime, latestExerciseTimeDetermination, )
supermod.SharedAmericanExercise.subclass = SharedAmericanExerciseSub
# end class SharedAmericanExerciseSub


class SimplePaymentSub(supermod.SimplePayment):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentAmount=None, paymentDate=None, extensiontype_=None):
        super(SimplePaymentSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentAmount, paymentDate, extensiontype_, )
supermod.SimplePayment.subclass = SimplePaymentSub
# end class SimplePaymentSub


class SplitSettlementSub(supermod.SplitSettlement):
    def __init__(self, splitSettlementAmount=None, beneficiaryBank=None, beneficiary=None):
        super(SplitSettlementSub, self).__init__(splitSettlementAmount, beneficiaryBank, beneficiary, )
supermod.SplitSettlement.subclass = SplitSettlementSub
# end class SplitSettlementSub


class SpreadScheduleSub(supermod.SpreadSchedule):
    def __init__(self, id=None, initialValue=None, step=None, type_=None):
        super(SpreadScheduleSub, self).__init__(id, initialValue, step, type_, )
supermod.SpreadSchedule.subclass = SpreadScheduleSub
# end class SpreadScheduleSub


class SpreadScheduleReferenceSub(supermod.SpreadScheduleReference):
    def __init__(self, href=None):
        super(SpreadScheduleReferenceSub, self).__init__(href, )
supermod.SpreadScheduleReference.subclass = SpreadScheduleReferenceSub
# end class SpreadScheduleReferenceSub


class SpreadScheduleTypeSub(supermod.SpreadScheduleType):
    def __init__(self, spreadScheduleTypeScheme='http://www.fpml.org/coding-scheme/spread-schedule-type', valueOf_=None):
        super(SpreadScheduleTypeSub, self).__init__(spreadScheduleTypeScheme, valueOf_, )
supermod.SpreadScheduleType.subclass = SpreadScheduleTypeSub
# end class SpreadScheduleTypeSub


class StepBaseSub(supermod.StepBase):
    def __init__(self, id=None, stepDate=None, extensiontype_=None):
        super(StepBaseSub, self).__init__(id, stepDate, extensiontype_, )
supermod.StepBase.subclass = StepBaseSub
# end class StepBaseSub


class StreetAddressSub(supermod.StreetAddress):
    def __init__(self, streetLine=None):
        super(StreetAddressSub, self).__init__(streetLine, )
supermod.StreetAddress.subclass = StreetAddressSub
# end class StreetAddressSub


class StrikeSub(supermod.Strike):
    def __init__(self, id=None, strikeRate=None, buyer=None, seller=None):
        super(StrikeSub, self).__init__(id, strikeRate, buyer, seller, )
supermod.Strike.subclass = StrikeSub
# end class StrikeSub


class StrikeScheduleSub(supermod.StrikeSchedule):
    def __init__(self, id=None, initialValue=None, step=None, buyer=None, seller=None):
        super(StrikeScheduleSub, self).__init__(id, initialValue, step, buyer, seller, )
supermod.StrikeSchedule.subclass = StrikeScheduleSub
# end class StrikeScheduleSub


class StubValueSub(supermod.StubValue):
    def __init__(self, floatingRate=None, stubRate=None, stubAmount=None, extensiontype_=None):
        super(StubValueSub, self).__init__(floatingRate, stubRate, stubAmount, extensiontype_, )
supermod.StubValue.subclass = StubValueSub
# end class StubValueSub


class StubFloatingRateSub(supermod.StubFloatingRate):
    def __init__(self, id=None, floatingRateIndex=None, indexTenor=None, floatingRateMultiplierSchedule=None, spreadSchedule=None, rateTreatment=None, capRateSchedule=None, floorRateSchedule=None, capFloorStraddle=None):
        super(StubFloatingRateSub, self).__init__(id, floatingRateIndex, indexTenor, floatingRateMultiplierSchedule, spreadSchedule, rateTreatment, capRateSchedule, floorRateSchedule, capFloorStraddle, )
supermod.StubFloatingRate.subclass = StubFloatingRateSub
# end class StubFloatingRateSub


class SupervisoryBodySub(supermod.SupervisoryBody):
    def __init__(self, supervisoryBodyScheme='http://www.fpml.org/coding-scheme/supervisory-body', valueOf_=None):
        super(SupervisoryBodySub, self).__init__(supervisoryBodyScheme, valueOf_, )
supermod.SupervisoryBody.subclass = SupervisoryBodySub
# end class SupervisoryBodySub


class TelephoneNumberSub(supermod.TelephoneNumber):
    def __init__(self, type_=None, number=None):
        super(TelephoneNumberSub, self).__init__(type_, number, )
supermod.TelephoneNumber.subclass = TelephoneNumberSub
# end class TelephoneNumberSub


class TimezoneLocationSub(supermod.TimezoneLocation):
    def __init__(self, timezoneLocationScheme='http://www.fpml.org/coding-scheme/external/tzdatabase', valueOf_=None):
        super(TimezoneLocationSub, self).__init__(timezoneLocationScheme, valueOf_, )
supermod.TimezoneLocation.subclass = TimezoneLocationSub
# end class TimezoneLocationSub


class TradeIdSub(supermod.TradeId):
    def __init__(self, tradeIdScheme=None, id=None, valueOf_=None):
        super(TradeIdSub, self).__init__(tradeIdScheme, id, valueOf_, )
supermod.TradeId.subclass = TradeIdSub
# end class TradeIdSub


class UnitSub(supermod.Unit):
    def __init__(self, unitScheme=None, valueOf_=None):
        super(UnitSub, self).__init__(unitScheme, valueOf_, )
supermod.Unit.subclass = UnitSub
# end class UnitSub


class IssuerIdSub(supermod.IssuerId):
    def __init__(self, issuerIdScheme=None, valueOf_=None):
        super(IssuerIdSub, self).__init__(issuerIdScheme, valueOf_, )
supermod.IssuerId.subclass = IssuerIdSub
# end class IssuerIdSub


class IssuerTradeIdSub(supermod.IssuerTradeId):
    def __init__(self, issuer=None, tradeId=None):
        super(IssuerTradeIdSub, self).__init__(issuer, tradeId, )
supermod.IssuerTradeId.subclass = IssuerTradeIdSub
# end class IssuerTradeIdSub


class ActualPriceSub(supermod.ActualPrice):
    def __init__(self, id=None, currency=None, amount=None, priceExpression=None):
        super(ActualPriceSub, self).__init__(id, currency, amount, priceExpression, )
supermod.ActualPrice.subclass = ActualPriceSub
# end class ActualPriceSub


class AnyAssetReferenceSub(supermod.AnyAssetReference):
    def __init__(self, href=None):
        super(AnyAssetReferenceSub, self).__init__(href, )
supermod.AnyAssetReference.subclass = AnyAssetReferenceSub
# end class AnyAssetReferenceSub


class AssetSub(supermod.Asset):
    def __init__(self, id=None, extensiontype_=None):
        super(AssetSub, self).__init__(id, extensiontype_, )
supermod.Asset.subclass = AssetSub
# end class AssetSub


class AssetMeasureTypeSub(supermod.AssetMeasureType):
    def __init__(self, assetMeasureScheme='http://www.fpml.org/coding-scheme/asset-measure', valueOf_=None):
        super(AssetMeasureTypeSub, self).__init__(assetMeasureScheme, valueOf_, )
supermod.AssetMeasureType.subclass = AssetMeasureTypeSub
# end class AssetMeasureTypeSub


class AssetPoolSub(supermod.AssetPool):
    def __init__(self, version=None, effectiveDate=None, initialFactor=None, currentFactor=None):
        super(AssetPoolSub, self).__init__(version, effectiveDate, initialFactor, currentFactor, )
supermod.AssetPool.subclass = AssetPoolSub
# end class AssetPoolSub


class AssetReferenceSub(supermod.AssetReference):
    def __init__(self, href=None):
        super(AssetReferenceSub, self).__init__(href, )
supermod.AssetReference.subclass = AssetReferenceSub
# end class AssetReferenceSub


class BasicQuotationSub(supermod.BasicQuotation):
    def __init__(self, id=None, value=None, measureType=None, quoteUnits=None, side=None, currency=None, currencyType=None, timing=None, businessCenter=None, exchangeId=None, informationSource=None, pricingModel=None, time=None, valuationDate=None, expiryTime=None, cashflowType=None):
        super(BasicQuotationSub, self).__init__(id, value, measureType, quoteUnits, side, currency, currencyType, timing, businessCenter, exchangeId, informationSource, pricingModel, time, valuationDate, expiryTime, cashflowType, )
supermod.BasicQuotation.subclass = BasicQuotationSub
# end class BasicQuotationSub


class BasketSub(supermod.Basket):
    def __init__(self, id=None, openUnits=None, basketConstituent=None, basketDivisor=None, basketVersion=None, basketName=None, basketId=None, basketCurrency=None):
        super(BasketSub, self).__init__(id, openUnits, basketConstituent, basketDivisor, basketVersion, basketName, basketId, basketCurrency, )
supermod.Basket.subclass = BasketSub
# end class BasketSub


class BasketConstituentSub(supermod.BasketConstituent):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, underlyingAsset=None, constituentWeight=None, dividendPayout=None, underlyerPrice=None, underlyerNotional=None, underlyerSpread=None, couponPayment=None, underlyerFinancing=None, underlyerLoanRate=None, underlyerCollateral=None):
        super(BasketConstituentSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, underlyingAsset, constituentWeight, dividendPayout, underlyerPrice, underlyerNotional, underlyerSpread, couponPayment, underlyerFinancing, underlyerLoanRate, underlyerCollateral, )
supermod.BasketConstituent.subclass = BasketConstituentSub
# end class BasketConstituentSub


class BasketIdSub(supermod.BasketId):
    def __init__(self, basketIdScheme=None, valueOf_=None):
        super(BasketIdSub, self).__init__(basketIdScheme, valueOf_, )
supermod.BasketId.subclass = BasketIdSub
# end class BasketIdSub


class BasketNameSub(supermod.BasketName):
    def __init__(self, basketNameScheme=None, valueOf_=None):
        super(BasketNameSub, self).__init__(basketNameScheme, valueOf_, )
supermod.BasketName.subclass = BasketNameSub
# end class BasketNameSub


class CashSub(supermod.Cash):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None):
        super(CashSub, self).__init__(id, instrumentId, description, currency, )
supermod.Cash.subclass = CashSub
# end class CashSub


class CommissionSub(supermod.Commission):
    def __init__(self, commissionDenomination=None, commissionAmount=None, currency=None, commissionPerTrade=None, fxRate=None):
        super(CommissionSub, self).__init__(commissionDenomination, commissionAmount, currency, commissionPerTrade, fxRate, )
supermod.Commission.subclass = CommissionSub
# end class CommissionSub


class CommodityBaseSub(supermod.CommodityBase):
    def __init__(self, commodityBaseScheme=None, valueOf_=None):
        super(CommodityBaseSub, self).__init__(commodityBaseScheme, valueOf_, )
supermod.CommodityBase.subclass = CommodityBaseSub
# end class CommodityBaseSub


class CommodityBusinessCalendarSub(supermod.CommodityBusinessCalendar):
    def __init__(self, commodityBusinessCalendarScheme='http://www.fpml.org/coding-scheme/commodity-business-calendar', valueOf_=None):
        super(CommodityBusinessCalendarSub, self).__init__(commodityBusinessCalendarScheme, valueOf_, )
supermod.CommodityBusinessCalendar.subclass = CommodityBusinessCalendarSub
# end class CommodityBusinessCalendarSub


class CommodityDetailsSub(supermod.CommodityDetails):
    def __init__(self, commodityDetailsScheme=None, valueOf_=None):
        super(CommodityDetailsSub, self).__init__(commodityDetailsScheme, valueOf_, )
supermod.CommodityDetails.subclass = CommodityDetailsSub
# end class CommodityDetailsSub


class CommodityInformationProviderSub(supermod.CommodityInformationProvider):
    def __init__(self, informationProviderScheme='http://www.fpml.org/coding-scheme/commodity-information-provider', valueOf_=None):
        super(CommodityInformationProviderSub, self).__init__(informationProviderScheme, valueOf_, )
supermod.CommodityInformationProvider.subclass = CommodityInformationProviderSub
# end class CommodityInformationProviderSub


class CommodityInformationSourceSub(supermod.CommodityInformationSource):
    def __init__(self, rateSource=None, rateSourcePage=None, rateSourcePageHeading=None):
        super(CommodityInformationSourceSub, self).__init__(rateSource, rateSourcePage, rateSourcePageHeading, )
supermod.CommodityInformationSource.subclass = CommodityInformationSourceSub
# end class CommodityInformationSourceSub


class ConstituentWeightSub(supermod.ConstituentWeight):
    def __init__(self, openUnits=None, basketPercentage=None, basketAmount=None):
        super(ConstituentWeightSub, self).__init__(openUnits, basketPercentage, basketAmount, )
supermod.ConstituentWeight.subclass = ConstituentWeightSub
# end class ConstituentWeightSub


class CouponTypeSub(supermod.CouponType):
    def __init__(self, couponTypeScheme='http://www.fpml.org/coding-scheme/coupon-type', valueOf_=None):
        super(CouponTypeSub, self).__init__(couponTypeScheme, valueOf_, )
supermod.CouponType.subclass = CouponTypeSub
# end class CouponTypeSub


class DeliveryNearbySub(supermod.DeliveryNearby):
    def __init__(self, id=None, deliveryNearbyMultiplier=None, deliveryNearbyType=None):
        super(DeliveryNearbySub, self).__init__(id, deliveryNearbyMultiplier, deliveryNearbyType, )
supermod.DeliveryNearby.subclass = DeliveryNearbySub
# end class DeliveryNearbySub


class DividendPayoutSub(supermod.DividendPayout):
    def __init__(self, dividendPayoutRatio=None, dividendPayoutRatioCash=None, dividendPayoutRatioNonCash=None, dividendPayoutConditions=None, dividendPayment=None):
        super(DividendPayoutSub, self).__init__(dividendPayoutRatio, dividendPayoutRatioCash, dividendPayoutRatioNonCash, dividendPayoutConditions, dividendPayment, )
supermod.DividendPayout.subclass = DividendPayoutSub
# end class DividendPayoutSub


class FacilityTypeSub(supermod.FacilityType):
    def __init__(self, facilityTypeScheme='http://www.fpml.org/coding-scheme/facility-type', valueOf_=None):
        super(FacilityTypeSub, self).__init__(facilityTypeScheme, valueOf_, )
supermod.FacilityType.subclass = FacilityTypeSub
# end class FacilityTypeSub


class FutureIdSub(supermod.FutureId):
    def __init__(self, futureIdScheme=None, valueOf_=None):
        super(FutureIdSub, self).__init__(futureIdScheme, valueOf_, )
supermod.FutureId.subclass = FutureIdSub
# end class FutureIdSub


class FxConversionSub(supermod.FxConversion):
    def __init__(self, amountRelativeTo=None, fxRate=None):
        super(FxConversionSub, self).__init__(amountRelativeTo, fxRate, )
supermod.FxConversion.subclass = FxConversionSub
# end class FxConversionSub


class IdentifiedAssetSub(supermod.IdentifiedAsset):
    def __init__(self, id=None, instrumentId=None, description=None, extensiontype_=None):
        super(IdentifiedAssetSub, self).__init__(id, instrumentId, description, extensiontype_, )
supermod.IdentifiedAsset.subclass = IdentifiedAssetSub
# end class IdentifiedAssetSub


class LienSub(supermod.Lien):
    def __init__(self, lienScheme='http://www.fpml.org/coding-scheme/designated-priority', valueOf_=None):
        super(LienSub, self).__init__(lienScheme, valueOf_, )
supermod.Lien.subclass = LienSub
# end class LienSub


class MortgageSectorSub(supermod.MortgageSector):
    def __init__(self, mortgageSectorScheme='http://www.fpml.org/coding-scheme/mortgage-sector', valueOf_=None):
        super(MortgageSectorSub, self).__init__(mortgageSectorScheme, valueOf_, )
supermod.MortgageSector.subclass = MortgageSectorSub
# end class MortgageSectorSub


class PendingPaymentSub(supermod.PendingPayment):
    def __init__(self, id=None, paymentDate=None, amount=None, accruedInterest=None):
        super(PendingPaymentSub, self).__init__(id, paymentDate, amount, accruedInterest, )
supermod.PendingPayment.subclass = PendingPaymentSub
# end class PendingPaymentSub


class PriceSub(supermod.Price):
    def __init__(self, commission=None, determinationMethod=None, grossPrice=None, netPrice=None, accruedInterestPrice=None, fxConversion=None, amountRelativeTo=None, cleanNetPrice=None, quotationCharacteristics=None, extensiontype_=None):
        super(PriceSub, self).__init__(commission, determinationMethod, grossPrice, netPrice, accruedInterestPrice, fxConversion, amountRelativeTo, cleanNetPrice, quotationCharacteristics, extensiontype_, )
supermod.Price.subclass = PriceSub
# end class PriceSub


class PriceQuoteUnitsSub(supermod.PriceQuoteUnits):
    def __init__(self, priceQuoteUnitsScheme='http://www.fpml.org/coding-scheme/price-quote-units', valueOf_=None):
        super(PriceQuoteUnitsSub, self).__init__(priceQuoteUnitsScheme, valueOf_, )
supermod.PriceQuoteUnits.subclass = PriceQuoteUnitsSub
# end class PriceQuoteUnitsSub


class PricingModelSub(supermod.PricingModel):
    def __init__(self, pricingModelScheme='http://www.fpml.org/coding-scheme/pricing-model', valueOf_=None):
        super(PricingModelSub, self).__init__(pricingModelScheme, valueOf_, )
supermod.PricingModel.subclass = PricingModelSub
# end class PricingModelSub


class QuantityUnitSub(supermod.QuantityUnit):
    def __init__(self, quantityUnitScheme='http://www.fpml.org/coding-scheme/price-quote-units', valueOf_=None):
        super(QuantityUnitSub, self).__init__(quantityUnitScheme, valueOf_, )
supermod.QuantityUnit.subclass = QuantityUnitSub
# end class QuantityUnitSub


class QuotationCharacteristicsSub(supermod.QuotationCharacteristics):
    def __init__(self, measureType=None, quoteUnits=None, side=None, currency=None, currencyType=None, timing=None, businessCenter=None, exchangeId=None, informationSource=None, pricingModel=None, time=None, valuationDate=None, expiryTime=None, cashflowType=None):
        super(QuotationCharacteristicsSub, self).__init__(measureType, quoteUnits, side, currency, currencyType, timing, businessCenter, exchangeId, informationSource, pricingModel, time, valuationDate, expiryTime, cashflowType, )
supermod.QuotationCharacteristics.subclass = QuotationCharacteristicsSub
# end class QuotationCharacteristicsSub


class QuoteTimingSub(supermod.QuoteTiming):
    def __init__(self, quoteTimingScheme='http://www.fpml.org/coding-scheme/quote-timing', valueOf_=None):
        super(QuoteTimingSub, self).__init__(quoteTimingScheme, valueOf_, )
supermod.QuoteTiming.subclass = QuoteTimingSub
# end class QuoteTimingSub


class ReportingCurrencyTypeSub(supermod.ReportingCurrencyType):
    def __init__(self, reportingCurrencyTypeScheme='http://www.fpml.org/coding-scheme/reporting-currency-type', valueOf_=None):
        super(ReportingCurrencyTypeSub, self).__init__(reportingCurrencyTypeScheme, valueOf_, )
supermod.ReportingCurrencyType.subclass = ReportingCurrencyTypeSub
# end class ReportingCurrencyTypeSub


class SingleUnderlyerSub(supermod.SingleUnderlyer):
    def __init__(self, underlyingAsset=None, openUnits=None, dividendPayout=None, couponPayment=None, averageDailyTradingVolume=None, depositoryReceipt=None):
        super(SingleUnderlyerSub, self).__init__(underlyingAsset, openUnits, dividendPayout, couponPayment, averageDailyTradingVolume, depositoryReceipt, )
supermod.SingleUnderlyer.subclass = SingleUnderlyerSub
# end class SingleUnderlyerSub


class UnderlyerSub(supermod.Underlyer):
    def __init__(self, singleUnderlyer=None, basket=None):
        super(UnderlyerSub, self).__init__(singleUnderlyer, basket, )
supermod.Underlyer.subclass = UnderlyerSub
# end class UnderlyerSub


class UnderlyingAssetSub(supermod.UnderlyingAsset):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, extensiontype_=None):
        super(UnderlyingAssetSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, extensiontype_, )
supermod.UnderlyingAsset.subclass = UnderlyingAssetSub
# end class UnderlyingAssetSub


class UnderlyingAssetTrancheSub(supermod.UnderlyingAssetTranche):
    def __init__(self, loanTrancheScheme=None, valueOf_=None):
        super(UnderlyingAssetTrancheSub, self).__init__(loanTrancheScheme, valueOf_, )
supermod.UnderlyingAssetTranche.subclass = UnderlyingAssetTrancheSub
# end class UnderlyingAssetTrancheSub


class UnderlyerLoanRateSub(supermod.UnderlyerLoanRate):
    def __init__(self, lossOfStockBorrow=None, maximumStockLoanRate=None, increasedCostOfStockBorrow=None, initialStockLoanRate=None):
        super(UnderlyerLoanRateSub, self).__init__(lossOfStockBorrow, maximumStockLoanRate, increasedCostOfStockBorrow, initialStockLoanRate, )
supermod.UnderlyerLoanRate.subclass = UnderlyerLoanRateSub
# end class UnderlyerLoanRateSub


class AbsoluteToleranceSub(supermod.AbsoluteTolerance):
    def __init__(self, positive=None, negative=None, unit=None, optionOwnerPartyReference=None):
        super(AbsoluteToleranceSub, self).__init__(positive, negative, unit, optionOwnerPartyReference, )
supermod.AbsoluteTolerance.subclass = AbsoluteToleranceSub
# end class AbsoluteToleranceSub


class BullionDeliveryLocationSub(supermod.BullionDeliveryLocation):
    def __init__(self, bullionDeliveryLocationScheme='http://www.fpml.org/coding-scheme/bullion-delivery-location', valueOf_=None):
        super(BullionDeliveryLocationSub, self).__init__(bullionDeliveryLocationScheme, valueOf_, )
supermod.BullionDeliveryLocation.subclass = BullionDeliveryLocationSub
# end class BullionDeliveryLocationSub


class CalculationPeriodsDatesReferenceSub(supermod.CalculationPeriodsDatesReference):
    def __init__(self, href=None):
        super(CalculationPeriodsDatesReferenceSub, self).__init__(href, )
supermod.CalculationPeriodsDatesReference.subclass = CalculationPeriodsDatesReferenceSub
# end class CalculationPeriodsDatesReferenceSub


class CalculationPeriodsReferenceSub(supermod.CalculationPeriodsReference):
    def __init__(self, href=None):
        super(CalculationPeriodsReferenceSub, self).__init__(href, )
supermod.CalculationPeriodsReference.subclass = CalculationPeriodsReferenceSub
# end class CalculationPeriodsReferenceSub


class CalculationPeriodsScheduleReferenceSub(supermod.CalculationPeriodsScheduleReference):
    def __init__(self, href=None):
        super(CalculationPeriodsScheduleReferenceSub, self).__init__(href, )
supermod.CalculationPeriodsScheduleReference.subclass = CalculationPeriodsScheduleReferenceSub
# end class CalculationPeriodsScheduleReferenceSub


class CoalAttributeDecimalSub(supermod.CoalAttributeDecimal):
    def __init__(self, standardContent=None, rejectionLimit=None):
        super(CoalAttributeDecimalSub, self).__init__(standardContent, rejectionLimit, )
supermod.CoalAttributeDecimal.subclass = CoalAttributeDecimalSub
# end class CoalAttributeDecimalSub


class CoalAttributePercentageSub(supermod.CoalAttributePercentage):
    def __init__(self, standardContent=None, rejectionLimit=None):
        super(CoalAttributePercentageSub, self).__init__(standardContent, rejectionLimit, )
supermod.CoalAttributePercentage.subclass = CoalAttributePercentageSub
# end class CoalAttributePercentageSub


class CoalDeliverySub(supermod.CoalDelivery):
    def __init__(self, deliveryPoint=None, deliveryAtSource=None, quantityVariationAdjustment=None, transportationEquipment=None, risk=None):
        super(CoalDeliverySub, self).__init__(deliveryPoint, deliveryAtSource, quantityVariationAdjustment, transportationEquipment, risk, )
supermod.CoalDelivery.subclass = CoalDeliverySub
# end class CoalDeliverySub


class CoalDeliveryPointSub(supermod.CoalDeliveryPoint):
    def __init__(self, deliveryPointScheme=None, valueOf_=None):
        super(CoalDeliveryPointSub, self).__init__(deliveryPointScheme, valueOf_, )
supermod.CoalDeliveryPoint.subclass = CoalDeliveryPointSub
# end class CoalDeliveryPointSub


class CoalProductSub(supermod.CoalProduct):
    def __init__(self, type_=None, coalProductSpecifications=None, source=None, sCoTASpecifications=None, btuQualityAdjustment=None, so2QualityAdjustment=None):
        super(CoalProductSub, self).__init__(type_, coalProductSpecifications, source, sCoTASpecifications, btuQualityAdjustment, so2QualityAdjustment, )
supermod.CoalProduct.subclass = CoalProductSub
# end class CoalProductSub


class CoalProductSourceSub(supermod.CoalProductSource):
    def __init__(self, commodityCoalProductSourceScheme='http://www.fpml.org/coding-scheme/commodity-coal-product-source', valueOf_=None):
        super(CoalProductSourceSub, self).__init__(commodityCoalProductSourceScheme, valueOf_, )
supermod.CoalProductSource.subclass = CoalProductSourceSub
# end class CoalProductSourceSub


class CoalProductSpecificationsSub(supermod.CoalProductSpecifications):
    def __init__(self, standardQuality=None, standardQualitySchedule=None):
        super(CoalProductSpecificationsSub, self).__init__(standardQuality, standardQualitySchedule, )
supermod.CoalProductSpecifications.subclass = CoalProductSpecificationsSub
# end class CoalProductSpecificationsSub


class CoalProductTypeSub(supermod.CoalProductType):
    def __init__(self, commodityCoalProductTypeScheme='http://www.fpml.org/coding-scheme/commodity-coal-product-type', valueOf_=None):
        super(CoalProductTypeSub, self).__init__(commodityCoalProductTypeScheme, valueOf_, )
supermod.CoalProductType.subclass = CoalProductTypeSub
# end class CoalProductTypeSub


class CoalQualityAdjustmentsSub(supermod.CoalQualityAdjustments):
    def __init__(self, commodityCoalQualityAdjustmentsScheme='http://www.fpml.org/coding-scheme/commodity-coal-quality-adjustments', valueOf_=None):
        super(CoalQualityAdjustmentsSub, self).__init__(commodityCoalQualityAdjustmentsScheme, valueOf_, )
supermod.CoalQualityAdjustments.subclass = CoalQualityAdjustmentsSub
# end class CoalQualityAdjustmentsSub


class CoalStandardQualitySub(supermod.CoalStandardQuality):
    def __init__(self, moisture=None, ash=None, sulfur=None, SO2=None, volatile=None, BTUperLB=None, topSize=None, finesPassingScreen=None, grindability=None, ashFusionTemperature=None, initialDeformation=None, softeningHeightWidth=None, softeningHeightHalfWidth=None, fluid=None):
        super(CoalStandardQualitySub, self).__init__(moisture, ash, sulfur, SO2, volatile, BTUperLB, topSize, finesPassingScreen, grindability, ashFusionTemperature, initialDeformation, softeningHeightWidth, softeningHeightHalfWidth, fluid, )
supermod.CoalStandardQuality.subclass = CoalStandardQualitySub
# end class CoalStandardQualitySub


class CoalStandardQualityScheduleSub(supermod.CoalStandardQualitySchedule):
    def __init__(self, StandardQualityStep=None, deliveryPeriodsReference=None, deliveryPeriodsScheduleReference=None):
        super(CoalStandardQualityScheduleSub, self).__init__(StandardQualityStep, deliveryPeriodsReference, deliveryPeriodsScheduleReference, )
supermod.CoalStandardQualitySchedule.subclass = CoalStandardQualityScheduleSub
# end class CoalStandardQualityScheduleSub


class CoalTransportationEquipmentSub(supermod.CoalTransportationEquipment):
    def __init__(self, commodityCoalTransportationEquipmentScheme='http://www.fpml.org/coding-scheme/commodity-coal-transportation-equipment', valueOf_=None):
        super(CoalTransportationEquipmentSub, self).__init__(commodityCoalTransportationEquipmentScheme, valueOf_, )
supermod.CoalTransportationEquipment.subclass = CoalTransportationEquipmentSub
# end class CoalTransportationEquipmentSub


class CommodityAmericanExerciseSub(supermod.CommodityAmericanExercise):
    def __init__(self, id=None, exercisePeriod=None, exerciseFrequency=None, latestExerciseTime=None, latestExerciseTimeDetermination=None, expirationTime=None, multipleExercise=None):
        super(CommodityAmericanExerciseSub, self).__init__(id, exercisePeriod, exerciseFrequency, latestExerciseTime, latestExerciseTimeDetermination, expirationTime, multipleExercise, )
supermod.CommodityAmericanExercise.subclass = CommodityAmericanExerciseSub
# end class CommodityAmericanExerciseSub


class CommodityBarrierSub(supermod.CommodityBarrier):
    def __init__(self, knock=None, featurePaymentAmount=None, trigger=None):
        super(CommodityBarrierSub, self).__init__(knock, featurePaymentAmount, trigger, )
supermod.CommodityBarrier.subclass = CommodityBarrierSub
# end class CommodityBarrierSub


class CommodityBasketSub(supermod.CommodityBasket):
    def __init__(self, basketName=None, basketId=None, notionalQuantityBasket=None, notionalAmountBasket=None):
        super(CommodityBasketSub, self).__init__(basketName, basketId, notionalQuantityBasket, notionalAmountBasket, )
supermod.CommodityBasket.subclass = CommodityBasketSub
# end class CommodityBasketSub


class CommodityBasketBaseSub(supermod.CommodityBasketBase):
    def __init__(self, id=None, extensiontype_=None):
        super(CommodityBasketBaseSub, self).__init__(id, extensiontype_, )
supermod.CommodityBasketBase.subclass = CommodityBasketBaseSub
# end class CommodityBasketBaseSub


class CommodityBasketByNotionalSub(supermod.CommodityBasketByNotional):
    def __init__(self, id=None, underlying=None):
        super(CommodityBasketByNotionalSub, self).__init__(id, underlying, )
supermod.CommodityBasketByNotional.subclass = CommodityBasketByNotionalSub
# end class CommodityBasketByNotionalSub


class CommodityBasketByPercentageSub(supermod.CommodityBasketByPercentage):
    def __init__(self, id=None, underlying=None, notionalAmount=None):
        super(CommodityBasketByPercentageSub, self).__init__(id, underlying, notionalAmount, )
supermod.CommodityBasketByPercentage.subclass = CommodityBasketByPercentageSub
# end class CommodityBasketByPercentageSub


class CommodityBasketUnderlyingBaseSub(supermod.CommodityBasketUnderlyingBase):
    def __init__(self, id=None, direction=None, commodity=None, pricingDates=None, averagingMethod=None, extensiontype_=None):
        super(CommodityBasketUnderlyingBaseSub, self).__init__(id, direction, commodity, pricingDates, averagingMethod, extensiontype_, )
supermod.CommodityBasketUnderlyingBase.subclass = CommodityBasketUnderlyingBaseSub
# end class CommodityBasketUnderlyingBaseSub


class CommodityBasketUnderlyingByNotionalSub(supermod.CommodityBasketUnderlyingByNotional):
    def __init__(self, id=None, direction=None, commodity=None, pricingDates=None, averagingMethod=None, fx=None, conversionFactor=None, notionalQuantitySchedule=None, notionalQuantity=None, settlementPeriodsNotionalQuantity=None, totalNotionalQuantity=None, quantityReference=None):
        super(CommodityBasketUnderlyingByNotionalSub, self).__init__(id, direction, commodity, pricingDates, averagingMethod, fx, conversionFactor, notionalQuantitySchedule, notionalQuantity, settlementPeriodsNotionalQuantity, totalNotionalQuantity, quantityReference, )
supermod.CommodityBasketUnderlyingByNotional.subclass = CommodityBasketUnderlyingByNotionalSub
# end class CommodityBasketUnderlyingByNotionalSub


class CommodityBasketUnderlyingByPercentageSub(supermod.CommodityBasketUnderlyingByPercentage):
    def __init__(self, id=None, direction=None, commodity=None, pricingDates=None, averagingMethod=None, constituentWeight=None):
        super(CommodityBasketUnderlyingByPercentageSub, self).__init__(id, direction, commodity, pricingDates, averagingMethod, constituentWeight, )
supermod.CommodityBasketUnderlyingByPercentage.subclass = CommodityBasketUnderlyingByPercentageSub
# end class CommodityBasketUnderlyingByPercentageSub


class CommodityCalculationPeriodsScheduleSub(supermod.CommodityCalculationPeriodsSchedule):
    def __init__(self, id=None, periodMultiplier=None, period=None, balanceOfFirstPeriod=None):
        super(CommodityCalculationPeriodsScheduleSub, self).__init__(id, periodMultiplier, period, balanceOfFirstPeriod, )
supermod.CommodityCalculationPeriodsSchedule.subclass = CommodityCalculationPeriodsScheduleSub
# end class CommodityCalculationPeriodsScheduleSub


class CommodityDeliveryPeriodsSub(supermod.CommodityDeliveryPeriods):
    def __init__(self, id=None, periods=None, periodsSchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, extensiontype_=None):
        super(CommodityDeliveryPeriodsSub, self).__init__(id, periods, periodsSchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, extensiontype_, )
supermod.CommodityDeliveryPeriods.subclass = CommodityDeliveryPeriodsSub
# end class CommodityDeliveryPeriodsSub


class CommodityDeliveryPointSub(supermod.CommodityDeliveryPoint):
    def __init__(self, deliveryPointScheme=None, valueOf_=None):
        super(CommodityDeliveryPointSub, self).__init__(deliveryPointScheme, valueOf_, )
supermod.CommodityDeliveryPoint.subclass = CommodityDeliveryPointSub
# end class CommodityDeliveryPointSub


class CommodityDeliveryRiskSub(supermod.CommodityDeliveryRisk):
    def __init__(self, deliveryRiskScheme='http://www.fpml.org/coding-scheme/commodity-delivery-risk', valueOf_=None):
        super(CommodityDeliveryRiskSub, self).__init__(deliveryRiskScheme, valueOf_, )
supermod.CommodityDeliveryRisk.subclass = CommodityDeliveryRiskSub
# end class CommodityDeliveryRiskSub


class CommodityDigitalSub(supermod.CommodityDigital):
    def __init__(self, trigger=None, featurePaymentAmount=None):
        super(CommodityDigitalSub, self).__init__(trigger, featurePaymentAmount, )
supermod.CommodityDigital.subclass = CommodityDigitalSub
# end class CommodityDigitalSub


class CommodityDigitalExerciseSub(supermod.CommodityDigitalExercise):
    def __init__(self, americanExercise=None, europeanExercise=None, automaticExercise=None, writtenConfirmation=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None):
        super(CommodityDigitalExerciseSub, self).__init__(americanExercise, europeanExercise, automaticExercise, writtenConfirmation, relativePaymentDates, paymentDates, masterAgreementPaymentDates, )
supermod.CommodityDigitalExercise.subclass = CommodityDigitalExerciseSub
# end class CommodityDigitalExerciseSub


class CommodityEuropeanExerciseSub(supermod.CommodityEuropeanExercise):
    def __init__(self, id=None, expirationDate=None, exerciseFrequency=None, expirationTime=None):
        super(CommodityEuropeanExerciseSub, self).__init__(id, expirationDate, exerciseFrequency, expirationTime, )
supermod.CommodityEuropeanExercise.subclass = CommodityEuropeanExerciseSub
# end class CommodityEuropeanExerciseSub


class CommodityExerciseSub(supermod.CommodityExercise):
    def __init__(self, americanExercise=None, europeanExercise=None, automaticExercise=None, writtenConfirmation=None, settlementCurrency=None, fx=None, conversionFactor=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None):
        super(CommodityExerciseSub, self).__init__(americanExercise, europeanExercise, automaticExercise, writtenConfirmation, settlementCurrency, fx, conversionFactor, relativePaymentDates, paymentDates, masterAgreementPaymentDates, )
supermod.CommodityExercise.subclass = CommodityExerciseSub
# end class CommodityExerciseSub


class CommodityExerciseBasketSub(supermod.CommodityExerciseBasket):
    def __init__(self, americanExercise=None, europeanExercise=None, automaticExercise=None, writtenConfirmation=None, settlementCurrency=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None):
        super(CommodityExerciseBasketSub, self).__init__(americanExercise, europeanExercise, automaticExercise, writtenConfirmation, settlementCurrency, relativePaymentDates, paymentDates, masterAgreementPaymentDates, )
supermod.CommodityExerciseBasket.subclass = CommodityExerciseBasketSub
# end class CommodityExerciseBasketSub


class CommodityExercisePeriodsSub(supermod.CommodityExercisePeriods):
    def __init__(self, commencementDate=None, expirationDate=None):
        super(CommodityExercisePeriodsSub, self).__init__(commencementDate, expirationDate, )
supermod.CommodityExercisePeriods.subclass = CommodityExercisePeriodsSub
# end class CommodityExercisePeriodsSub


class CommodityExpireRelativeToEventSub(supermod.CommodityExpireRelativeToEvent):
    def __init__(self, commodityExpireRelativeToEventScheme='http://www.fpml.org/coding-scheme/commodity-expire-relative-to-event', valueOf_=None):
        super(CommodityExpireRelativeToEventSub, self).__init__(commodityExpireRelativeToEventScheme, valueOf_, )
supermod.CommodityExpireRelativeToEvent.subclass = CommodityExpireRelativeToEventSub
# end class CommodityExpireRelativeToEventSub


class CommodityFixedInterestCalculationSub(supermod.CommodityFixedInterestCalculation):
    def __init__(self, fixedRate=None, dayCountFraction=None):
        super(CommodityFixedInterestCalculationSub, self).__init__(fixedRate, dayCountFraction, )
supermod.CommodityFixedInterestCalculation.subclass = CommodityFixedInterestCalculationSub
# end class CommodityFixedInterestCalculationSub


class CommodityFixedPriceScheduleSub(supermod.CommodityFixedPriceSchedule):
    def __init__(self, fixedPriceStep=None, worldscaleRateStep=None, contractRateStep=None, settlementPeriodsPriceSchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None):
        super(CommodityFixedPriceScheduleSub, self).__init__(fixedPriceStep, worldscaleRateStep, contractRateStep, settlementPeriodsPriceSchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, )
supermod.CommodityFixedPriceSchedule.subclass = CommodityFixedPriceScheduleSub
# end class CommodityFixedPriceScheduleSub


class CommodityForwardSub(supermod.CommodityForward):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, valueDate=None, fixedLeg=None, averagePriceLeg=None, commodityForwardLeg=None, commonPricing=None, marketDisruption=None, settlementDisruption=None, rounding=None):
        super(CommodityForwardSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, valueDate, fixedLeg, averagePriceLeg, commodityForwardLeg, commonPricing, marketDisruption, settlementDisruption, rounding, )
supermod.CommodityForward.subclass = CommodityForwardSub
# end class CommodityForwardSub


class CommodityForwardLegSub(supermod.CommodityForwardLeg):
    def __init__(self, id=None, extensiontype_=None):
        super(CommodityForwardLegSub, self).__init__(id, extensiontype_, )
supermod.CommodityForwardLeg.subclass = CommodityForwardLegSub
# end class CommodityForwardLegSub


class CommodityFrequencyTypeSub(supermod.CommodityFrequencyType):
    def __init__(self, commodityFrequencyTypeScheme='http://www.fpml.org/coding-scheme/commodity-frequency-type', valueOf_=None):
        super(CommodityFrequencyTypeSub, self).__init__(commodityFrequencyTypeScheme, valueOf_, )
supermod.CommodityFrequencyType.subclass = CommodityFrequencyTypeSub
# end class CommodityFrequencyTypeSub


class CommodityFxSub(supermod.CommodityFx):
    def __init__(self, primaryRateSource=None, secondaryRateSource=None, fxType=None, averagingMethod=None, fixingTime=None, fxObservationDates=None, dayType=None, dayDistribution=None, dayCount=None, dayOfWeek=None, dayNumber=None, businessDayConvention=None, lag=None, lagReference=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None):
        super(CommodityFxSub, self).__init__(primaryRateSource, secondaryRateSource, fxType, averagingMethod, fixingTime, fxObservationDates, dayType, dayDistribution, dayCount, dayOfWeek, dayNumber, businessDayConvention, lag, lagReference, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, )
supermod.CommodityFx.subclass = CommodityFxSub
# end class CommodityFxSub


class CommodityFxTypeSub(supermod.CommodityFxType):
    def __init__(self, commodityFxTypeScheme='http://www.fpml.org/coding-scheme/commodity-fx-type', valueOf_=None):
        super(CommodityFxTypeSub, self).__init__(commodityFxTypeScheme, valueOf_, )
supermod.CommodityFxType.subclass = CommodityFxTypeSub
# end class CommodityFxTypeSub


class CommodityHubSub(supermod.CommodityHub):
    def __init__(self, partyReference=None, accountReference=None, hubCode=None):
        super(CommodityHubSub, self).__init__(partyReference, accountReference, hubCode, )
supermod.CommodityHub.subclass = CommodityHubSub
# end class CommodityHubSub


class CommodityHubCodeSub(supermod.CommodityHubCode):
    def __init__(self, hubCodeScheme=None, valueOf_=None):
        super(CommodityHubCodeSub, self).__init__(hubCodeScheme, valueOf_, )
supermod.CommodityHubCode.subclass = CommodityHubCodeSub
# end class CommodityHubCodeSub


class CommodityMarketDisruptionSub(supermod.CommodityMarketDisruption):
    def __init__(self, marketDisruptionEvents=None, additionalMarketDisruptionEvent=None, marketDisruptionEvent=None, disruptionFallbacks=None, disruptionFallback=None, fallbackReferencePrice=None, maximumNumberOfDaysOfDisruption=None, priceMaterialityPercentage=None, minimumFuturesContracts=None):
        super(CommodityMarketDisruptionSub, self).__init__(marketDisruptionEvents, additionalMarketDisruptionEvent, marketDisruptionEvent, disruptionFallbacks, disruptionFallback, fallbackReferencePrice, maximumNumberOfDaysOfDisruption, priceMaterialityPercentage, minimumFuturesContracts, )
supermod.CommodityMarketDisruption.subclass = CommodityMarketDisruptionSub
# end class CommodityMarketDisruptionSub


class CommodityMetalBrandSub(supermod.CommodityMetalBrand):
    def __init__(self, name=None, brandManager=None, country=None, producer=None):
        super(CommodityMetalBrandSub, self).__init__(name, brandManager, country, producer, )
supermod.CommodityMetalBrand.subclass = CommodityMetalBrandSub
# end class CommodityMetalBrandSub


class CommodityMetalBrandManagerSub(supermod.CommodityMetalBrandManager):
    def __init__(self, commodityMetalBrandManagerScheme='http://www.fpml.org/coding-scheme/commodity-metal-brand-manager', valueOf_=None):
        super(CommodityMetalBrandManagerSub, self).__init__(commodityMetalBrandManagerScheme, valueOf_, )
supermod.CommodityMetalBrandManager.subclass = CommodityMetalBrandManagerSub
# end class CommodityMetalBrandManagerSub


class CommodityMetalBrandNameSub(supermod.CommodityMetalBrandName):
    def __init__(self, commodityMetalBrandNameScheme='http://www.fpml.org/coding-scheme/commodity-metal-brand-name', valueOf_=None):
        super(CommodityMetalBrandNameSub, self).__init__(commodityMetalBrandNameScheme, valueOf_, )
supermod.CommodityMetalBrandName.subclass = CommodityMetalBrandNameSub
# end class CommodityMetalBrandNameSub


class CommodityMetalGradeSub(supermod.CommodityMetalGrade):
    def __init__(self, commodityMetalGradeScheme=None, valueOf_=None):
        super(CommodityMetalGradeSub, self).__init__(commodityMetalGradeScheme, valueOf_, )
supermod.CommodityMetalGrade.subclass = CommodityMetalGradeSub
# end class CommodityMetalGradeSub


class CommodityMetalProducerSub(supermod.CommodityMetalProducer):
    def __init__(self, commodityMetalProducerScheme=None, valueOf_=None):
        super(CommodityMetalProducerSub, self).__init__(commodityMetalProducerScheme, valueOf_, )
supermod.CommodityMetalProducer.subclass = CommodityMetalProducerSub
# end class CommodityMetalProducerSub


class CommodityMetalShapeSub(supermod.CommodityMetalShape):
    def __init__(self, commodityMetalShapeScheme='http://www.fpml.org/coding-scheme/commodity-metal-shape', valueOf_=None):
        super(CommodityMetalShapeSub, self).__init__(commodityMetalShapeScheme, valueOf_, )
supermod.CommodityMetalShape.subclass = CommodityMetalShapeSub
# end class CommodityMetalShapeSub


class CommodityMultipleExerciseSub(supermod.CommodityMultipleExercise):
    def __init__(self, integralMultipleQuantity=None, minimumNotionalQuantity=None):
        super(CommodityMultipleExerciseSub, self).__init__(integralMultipleQuantity, minimumNotionalQuantity, )
supermod.CommodityMultipleExercise.subclass = CommodityMultipleExerciseSub
# end class CommodityMultipleExerciseSub


class CommodityNotionalAmountSub(supermod.CommodityNotionalAmount):
    def __init__(self, id=None, currency=None, amount=None, reinvestmentFeature=None):
        super(CommodityNotionalAmountSub, self).__init__(id, currency, amount, reinvestmentFeature, )
supermod.CommodityNotionalAmount.subclass = CommodityNotionalAmountSub
# end class CommodityNotionalAmountSub


class CommodityNotionalAmountReferenceSub(supermod.CommodityNotionalAmountReference):
    def __init__(self, href=None):
        super(CommodityNotionalAmountReferenceSub, self).__init__(href, )
supermod.CommodityNotionalAmountReference.subclass = CommodityNotionalAmountReferenceSub
# end class CommodityNotionalAmountReferenceSub


class CommodityNotionalQuantitySub(supermod.CommodityNotionalQuantity):
    def __init__(self, id=None, quantityUnit=None, quantityFrequency=None, quantity=None, extensiontype_=None):
        super(CommodityNotionalQuantitySub, self).__init__(id, quantityUnit, quantityFrequency, quantity, extensiontype_, )
supermod.CommodityNotionalQuantity.subclass = CommodityNotionalQuantitySub
# end class CommodityNotionalQuantitySub


class CommodityNotionalQuantityScheduleSub(supermod.CommodityNotionalQuantitySchedule):
    def __init__(self, id=None, notionalStep=None, settlementPeriodsNotionalQuantitySchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None):
        super(CommodityNotionalQuantityScheduleSub, self).__init__(id, notionalStep, settlementPeriodsNotionalQuantitySchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, )
supermod.CommodityNotionalQuantitySchedule.subclass = CommodityNotionalQuantityScheduleSub
# end class CommodityNotionalQuantityScheduleSub


class CommodityOptionSub(supermod.CommodityOption):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, optionType=None, commodity=None, effectiveDate=None, terminationDate=None, calculationPeriodsSchedule=None, calculationPeriods=None, pricingDates=None, averagingMethod=None, barrier=None, notionalQuantitySchedule=None, notionalQuantity=None, settlementPeriodsNotionalQuantity=None, totalNotionalQuantity=None, quantityReference=None, exercise=None, strikePricePerUnit=None, strikePricePerUnitSchedule=None, floatingStrikePricePerUnit=None, floatingStrikePricePerUnitSchedule=None, commoditySwap=None, commodityForward=None, physicalExercise=None, weatherCalculationPeriods=None, weatherCalculationPeriodsReference=None, weatherNotionalAmount=None, weatherIndexStrikeLevel=None, calculation=None, weatherIndexData=None, premium=None, commonPricing=None, marketDisruption=None, settlementDisruption=None, rounding=None):
        super(CommodityOptionSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, optionType, commodity, effectiveDate, terminationDate, calculationPeriodsSchedule, calculationPeriods, pricingDates, averagingMethod, barrier, notionalQuantitySchedule, notionalQuantity, settlementPeriodsNotionalQuantity, totalNotionalQuantity, quantityReference, exercise, strikePricePerUnit, strikePricePerUnitSchedule, floatingStrikePricePerUnit, floatingStrikePricePerUnitSchedule, commoditySwap, commodityForward, physicalExercise, weatherCalculationPeriods, weatherCalculationPeriodsReference, weatherNotionalAmount, weatherIndexStrikeLevel, calculation, weatherIndexData, premium, commonPricing, marketDisruption, settlementDisruption, rounding, )
supermod.CommodityOption.subclass = CommodityOptionSub
# end class CommodityOptionSub


class CommodityPayRelativeToEventSub(supermod.CommodityPayRelativeToEvent):
    def __init__(self, commodityPayRelativeToEventScheme='http://www.fpml.org/coding-scheme/commodity-pay-relative-to-event', valueOf_=None):
        super(CommodityPayRelativeToEventSub, self).__init__(commodityPayRelativeToEventScheme, valueOf_, )
supermod.CommodityPayRelativeToEvent.subclass = CommodityPayRelativeToEventSub
# end class CommodityPayRelativeToEventSub


class CommodityPerformanceSwapBaseSub(supermod.CommodityPerformanceSwapBase):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, effectiveDate=None, terminationDate=None, settlementCurrency=None, commodityPerformanceSwapLeg=None, commonPricing=None, marketDisruption=None, settlementDisruption=None, rounding=None, extensiontype_=None):
        super(CommodityPerformanceSwapBaseSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, effectiveDate, terminationDate, settlementCurrency, commodityPerformanceSwapLeg, commonPricing, marketDisruption, settlementDisruption, rounding, extensiontype_, )
supermod.CommodityPerformanceSwapBase.subclass = CommodityPerformanceSwapBaseSub
# end class CommodityPerformanceSwapBaseSub


class CommodityPerformanceSwapEarlyTerminationSub(supermod.CommodityPerformanceSwapEarlyTermination):
    def __init__(self, partyReference=None, startingDate=None):
        super(CommodityPerformanceSwapEarlyTerminationSub, self).__init__(partyReference, startingDate, )
supermod.CommodityPerformanceSwapEarlyTermination.subclass = CommodityPerformanceSwapEarlyTerminationSub
# end class CommodityPerformanceSwapEarlyTerminationSub


class CommodityPerformanceSwapLegSub(supermod.CommodityPerformanceSwapLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, extensiontype_=None):
        super(CommodityPerformanceSwapLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, extensiontype_, )
supermod.CommodityPerformanceSwapLeg.subclass = CommodityPerformanceSwapLegSub
# end class CommodityPerformanceSwapLegSub


class CommodityPhysicalAmericanExerciseSub(supermod.CommodityPhysicalAmericanExercise):
    def __init__(self, id=None, commencementDates=None, expirationDates=None, relativeCommencementDates=None, relativeExpirationDates=None, latestExerciseTime=None, expirationTime=None):
        super(CommodityPhysicalAmericanExerciseSub, self).__init__(id, commencementDates, expirationDates, relativeCommencementDates, relativeExpirationDates, latestExerciseTime, expirationTime, )
supermod.CommodityPhysicalAmericanExercise.subclass = CommodityPhysicalAmericanExerciseSub
# end class CommodityPhysicalAmericanExerciseSub


class CommodityPhysicalEuropeanExerciseSub(supermod.CommodityPhysicalEuropeanExercise):
    def __init__(self, id=None, expirationDate=None, expirationDates=None, relativeExpirationDates=None, expirationTime=None):
        super(CommodityPhysicalEuropeanExerciseSub, self).__init__(id, expirationDate, expirationDates, relativeExpirationDates, expirationTime, )
supermod.CommodityPhysicalEuropeanExercise.subclass = CommodityPhysicalEuropeanExerciseSub
# end class CommodityPhysicalEuropeanExerciseSub


class CommodityPhysicalExerciseSub(supermod.CommodityPhysicalExercise):
    def __init__(self, americanExercise=None, europeanExercise=None, automaticExercise=None, writtenConfirmation=None, clearingInstructions=None):
        super(CommodityPhysicalExerciseSub, self).__init__(americanExercise, europeanExercise, automaticExercise, writtenConfirmation, clearingInstructions, )
supermod.CommodityPhysicalExercise.subclass = CommodityPhysicalExerciseSub
# end class CommodityPhysicalExerciseSub


class CommodityPhysicalQuantityBaseSub(supermod.CommodityPhysicalQuantityBase):
    def __init__(self, id=None, extensiontype_=None):
        super(CommodityPhysicalQuantityBaseSub, self).__init__(id, extensiontype_, )
supermod.CommodityPhysicalQuantityBase.subclass = CommodityPhysicalQuantityBaseSub
# end class CommodityPhysicalQuantityBaseSub


class CommodityPhysicalQuantityScheduleSub(supermod.CommodityPhysicalQuantitySchedule):
    def __init__(self, id=None, quantityStep=None, deliveryPeriodsReference=None, deliveryPeriodsScheduleReference=None, extensiontype_=None):
        super(CommodityPhysicalQuantityScheduleSub, self).__init__(id, quantityStep, deliveryPeriodsReference, deliveryPeriodsScheduleReference, extensiontype_, )
supermod.CommodityPhysicalQuantitySchedule.subclass = CommodityPhysicalQuantityScheduleSub
# end class CommodityPhysicalQuantityScheduleSub


class CommodityPipelineSub(supermod.CommodityPipeline):
    def __init__(self, pipelineScheme=None, valueOf_=None):
        super(CommodityPipelineSub, self).__init__(pipelineScheme, valueOf_, )
supermod.CommodityPipeline.subclass = CommodityPipelineSub
# end class CommodityPipelineSub


class CommodityPipelineCycleSub(supermod.CommodityPipelineCycle):
    def __init__(self, pipelineCycleScheme=None, valueOf_=None):
        super(CommodityPipelineCycleSub, self).__init__(pipelineCycleScheme, valueOf_, )
supermod.CommodityPipelineCycle.subclass = CommodityPipelineCycleSub
# end class CommodityPipelineCycleSub


class CommodityPricingDatesSub(supermod.CommodityPricingDates):
    def __init__(self, id=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, lag=None, dayType=None, dayDistribution=None, dayCount=None, dayOfWeek=None, dayNumber=None, businessDayConvention=None, businessCalendar=None, calendarSource=None, settlementPeriods=None, settlementPeriodsReference=None, pricingDates=None):
        super(CommodityPricingDatesSub, self).__init__(id, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, lag, dayType, dayDistribution, dayCount, dayOfWeek, dayNumber, businessDayConvention, businessCalendar, calendarSource, settlementPeriods, settlementPeriodsReference, pricingDates, )
supermod.CommodityPricingDates.subclass = CommodityPricingDatesSub
# end class CommodityPricingDatesSub


class CommodityProductGradeSub(supermod.CommodityProductGrade):
    def __init__(self, productGradeScheme='http://www.fpml.org/coding-scheme/commodity-oil-product-grade', valueOf_=None):
        super(CommodityProductGradeSub, self).__init__(productGradeScheme, valueOf_, )
supermod.CommodityProductGrade.subclass = CommodityProductGradeSub
# end class CommodityProductGradeSub


class CommodityQuantityFrequencySub(supermod.CommodityQuantityFrequency):
    def __init__(self, quantityFrequencyScheme='http://www.fpml.org/coding-scheme/commodity-quantity-frequency', valueOf_=None):
        super(CommodityQuantityFrequencySub, self).__init__(quantityFrequencyScheme, valueOf_, )
supermod.CommodityQuantityFrequency.subclass = CommodityQuantityFrequencySub
# end class CommodityQuantityFrequencySub


class CommodityRelativeExpirationDatesSub(supermod.CommodityRelativeExpirationDates):
    def __init__(self, id=None, expireRelativeToEvent=None, expirationDateOffset=None, businessCentersReference=None, businessCenters=None):
        super(CommodityRelativeExpirationDatesSub, self).__init__(id, expireRelativeToEvent, expirationDateOffset, businessCentersReference, businessCenters, )
supermod.CommodityRelativeExpirationDates.subclass = CommodityRelativeExpirationDatesSub
# end class CommodityRelativeExpirationDatesSub


class CommodityRelativePaymentDatesSub(supermod.CommodityRelativePaymentDates):
    def __init__(self, id=None, payRelativeTo=None, payRelativeToEvent=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, paymentDaysOffset=None, businessCentersReference=None, businessCenters=None):
        super(CommodityRelativePaymentDatesSub, self).__init__(id, payRelativeTo, payRelativeToEvent, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, paymentDaysOffset, businessCentersReference, businessCenters, )
supermod.CommodityRelativePaymentDates.subclass = CommodityRelativePaymentDatesSub
# end class CommodityRelativePaymentDatesSub


class CommodityReturnCalculationSub(supermod.CommodityReturnCalculation):
    def __init__(self, formula=None, pricingDates=None, valuationDates=None, initialPrice=None):
        super(CommodityReturnCalculationSub, self).__init__(formula, pricingDates, valuationDates, initialPrice, )
supermod.CommodityReturnCalculation.subclass = CommodityReturnCalculationSub
# end class CommodityReturnCalculationSub


class CommodityReturnLegSub(supermod.CommodityReturnLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, calculationDates=None, calculationPeriods=None, calculationPeriodsSchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None, commodity=None, commodityBasket=None, notionalAmount=None, notionalAmountReference=None, commodityReturnCalculation=None):
        super(CommodityReturnLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, calculationDates, calculationPeriods, calculationPeriodsSchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, relativePaymentDates, paymentDates, masterAgreementPaymentDates, commodity, commodityBasket, notionalAmount, notionalAmountReference, commodityReturnCalculation, )
supermod.CommodityReturnLeg.subclass = CommodityReturnLegSub
# end class CommodityReturnLegSub


class CommoditySettlementPeriodsNotionalQuantitySub(supermod.CommoditySettlementPeriodsNotionalQuantity):
    def __init__(self, id=None, quantityUnit=None, quantityFrequency=None, quantity=None, settlementPeriodsReference=None):
        super(CommoditySettlementPeriodsNotionalQuantitySub, self).__init__(id, quantityUnit, quantityFrequency, quantity, settlementPeriodsReference, )
supermod.CommoditySettlementPeriodsNotionalQuantity.subclass = CommoditySettlementPeriodsNotionalQuantitySub
# end class CommoditySettlementPeriodsNotionalQuantitySub


class CommoditySettlementPeriodsNotionalQuantityScheduleSub(supermod.CommoditySettlementPeriodsNotionalQuantitySchedule):
    def __init__(self, settlementPeriodsNotionalQuantityStep=None, settlementPeriodsReference=None):
        super(CommoditySettlementPeriodsNotionalQuantityScheduleSub, self).__init__(settlementPeriodsNotionalQuantityStep, settlementPeriodsReference, )
supermod.CommoditySettlementPeriodsNotionalQuantitySchedule.subclass = CommoditySettlementPeriodsNotionalQuantityScheduleSub
# end class CommoditySettlementPeriodsNotionalQuantityScheduleSub


class CommoditySettlementPeriodsPriceScheduleSub(supermod.CommoditySettlementPeriodsPriceSchedule):
    def __init__(self, settlementPeriodsPriceStep=None, settlementPeriodsReference=None):
        super(CommoditySettlementPeriodsPriceScheduleSub, self).__init__(settlementPeriodsPriceStep, settlementPeriodsReference, )
supermod.CommoditySettlementPeriodsPriceSchedule.subclass = CommoditySettlementPeriodsPriceScheduleSub
# end class CommoditySettlementPeriodsPriceScheduleSub


class CommoditySpreadScheduleSub(supermod.CommoditySpreadSchedule):
    def __init__(self, spreadStep=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None):
        super(CommoditySpreadScheduleSub, self).__init__(spreadStep, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, )
supermod.CommoditySpreadSchedule.subclass = CommoditySpreadScheduleSub
# end class CommoditySpreadScheduleSub


class CommodityStartingDateSub(supermod.CommodityStartingDate):
    def __init__(self, dateRelativeTo=None, adjustableDate=None):
        super(CommodityStartingDateSub, self).__init__(dateRelativeTo, adjustableDate, )
supermod.CommodityStartingDate.subclass = CommodityStartingDateSub
# end class CommodityStartingDateSub


class CommodityStrikeScheduleSub(supermod.CommodityStrikeSchedule):
    def __init__(self, strikePricePerUnitStep=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None):
        super(CommodityStrikeScheduleSub, self).__init__(strikePricePerUnitStep, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, )
supermod.CommodityStrikeSchedule.subclass = CommodityStrikeScheduleSub
# end class CommodityStrikeScheduleSub


class CommoditySwapSub(supermod.CommoditySwap):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, effectiveDate=None, terminationDate=None, settlementCurrency=None, commoditySwapLeg=None, weatherLeg=None, commonPricing=None, marketDisruption=None, settlementDisruption=None, rounding=None):
        super(CommoditySwapSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, effectiveDate, terminationDate, settlementCurrency, commoditySwapLeg, weatherLeg, commonPricing, marketDisruption, settlementDisruption, rounding, )
supermod.CommoditySwap.subclass = CommoditySwapSub
# end class CommoditySwapSub


class CommoditySwapLegSub(supermod.CommoditySwapLeg):
    def __init__(self, id=None, extensiontype_=None):
        super(CommoditySwapLegSub, self).__init__(id, extensiontype_, )
supermod.CommoditySwapLeg.subclass = CommoditySwapLegSub
# end class CommoditySwapLegSub


class CommoditySwaptionSub(supermod.CommoditySwaption):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, optionType=None, commoditySwap=None, physicalExercise=None, premium=None, commonPricing=None, marketDisruption=None, settlementDisruption=None, rounding=None):
        super(CommoditySwaptionSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, optionType, commoditySwap, physicalExercise, premium, commonPricing, marketDisruption, settlementDisruption, rounding, )
supermod.CommoditySwaption.subclass = CommoditySwaptionSub
# end class CommoditySwaptionSub


class CommoditySwaptionUnderlyingSub(supermod.CommoditySwaptionUnderlying):
    def __init__(self, effectiveDate=None, terminationDate=None, settlementCurrency=None, commoditySwapLeg=None, weatherLeg=None, commonPricing=None, marketDisruption=None, settlementDisruption=None, rounding=None):
        super(CommoditySwaptionUnderlyingSub, self).__init__(effectiveDate, terminationDate, settlementCurrency, commoditySwapLeg, weatherLeg, commonPricing, marketDisruption, settlementDisruption, rounding, )
supermod.CommoditySwaptionUnderlying.subclass = CommoditySwaptionUnderlyingSub
# end class CommoditySwaptionUnderlyingSub


class CommodityTriggerSub(supermod.CommodityTrigger):
    def __init__(self, levelQuantity=None, levelUnit=None, levelPercentage=None, levelPrice=None, triggerType=None):
        super(CommodityTriggerSub, self).__init__(levelQuantity, levelUnit, levelPercentage, levelPrice, triggerType, )
supermod.CommodityTrigger.subclass = CommodityTriggerSub
# end class CommodityTriggerSub


class CommodityValuationDatesSub(supermod.CommodityValuationDates):
    def __init__(self, id=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, lag=None, dayType=None, dayDistribution=None, dayCount=None, dayOfWeek=None, dayNumber=None, businessDayConvention=None, businessCalendar=None, calendarSource=None, settlementPeriods=None, settlementPeriodsReference=None, valuationDates=None):
        super(CommodityValuationDatesSub, self).__init__(id, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, lag, dayType, dayDistribution, dayCount, dayOfWeek, dayNumber, businessDayConvention, businessCalendar, calendarSource, settlementPeriods, settlementPeriodsReference, valuationDates, )
supermod.CommodityValuationDates.subclass = CommodityValuationDatesSub
# end class CommodityValuationDatesSub


class CommodityVarianceLegSub(supermod.CommodityVarianceLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, calculationDates=None, calculationPeriods=None, calculationPeriodsSchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None, commodity=None, commodityBasket=None, notionalAmount=None, notionalAmountReference=None, varianceStrikePrice=None, volatilityStrikePrice=None, varianceCalculation=None):
        super(CommodityVarianceLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, calculationDates, calculationPeriods, calculationPeriodsSchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, relativePaymentDates, paymentDates, masterAgreementPaymentDates, commodity, commodityBasket, notionalAmount, notionalAmountReference, varianceStrikePrice, volatilityStrikePrice, varianceCalculation, )
supermod.CommodityVarianceLeg.subclass = CommodityVarianceLegSub
# end class CommodityVarianceLegSub


class CommodityVarianceCalculationSub(supermod.CommodityVarianceCalculation):
    def __init__(self, pricingDates=None, valuationDates=None, annualizationFactor=None, nAdjustment=None):
        super(CommodityVarianceCalculationSub, self).__init__(pricingDates, valuationDates, annualizationFactor, nAdjustment, )
supermod.CommodityVarianceCalculation.subclass = CommodityVarianceCalculationSub
# end class CommodityVarianceCalculationSub


class DataProviderSub(supermod.DataProvider):
    def __init__(self, weatherDataProviderScheme='http://www.fpml.org/coding-scheme/weather-data-provider', id=None, valueOf_=None):
        super(DataProviderSub, self).__init__(weatherDataProviderScheme, id, valueOf_, )
supermod.DataProvider.subclass = DataProviderSub
# end class DataProviderSub


class DisruptionFallbackSub(supermod.DisruptionFallback):
    def __init__(self, commodityMarketDisruptionFallbackScheme='http://www.fpml.org/coding-scheme/commodity-market-disruption-fallback', valueOf_=None):
        super(DisruptionFallbackSub, self).__init__(commodityMarketDisruptionFallbackScheme, valueOf_, )
supermod.DisruptionFallback.subclass = DisruptionFallbackSub
# end class DisruptionFallbackSub


class EEPParametersSub(supermod.EEPParameters):
    def __init__(self, eEPApplicable=None, riskPeriod=None, equivalentApplicable=None, penaltyApplicable=None):
        super(EEPParametersSub, self).__init__(eEPApplicable, riskPeriod, equivalentApplicable, penaltyApplicable, )
supermod.EEPParameters.subclass = EEPParametersSub
# end class EEPParametersSub


class EEPRiskPeriodSub(supermod.EEPRiskPeriod):
    def __init__(self, startDate=None, endDate=None):
        super(EEPRiskPeriodSub, self).__init__(startDate, endDate, )
supermod.EEPRiskPeriod.subclass = EEPRiskPeriodSub
# end class EEPRiskPeriodSub


class ElectricityDeliverySub(supermod.ElectricityDelivery):
    def __init__(self, deliveryPoint=None, deliveryType=None, transmissionContingency=None, interconnectionPoint=None, deliveryZone=None, electingPartyReference=None):
        super(ElectricityDeliverySub, self).__init__(deliveryPoint, deliveryType, transmissionContingency, interconnectionPoint, deliveryZone, electingPartyReference, )
supermod.ElectricityDelivery.subclass = ElectricityDeliverySub
# end class ElectricityDeliverySub


class ElectricityDeliveryFirmSub(supermod.ElectricityDeliveryFirm):
    def __init__(self, forceMajeure=None):
        super(ElectricityDeliveryFirmSub, self).__init__(forceMajeure, )
supermod.ElectricityDeliveryFirm.subclass = ElectricityDeliveryFirmSub
# end class ElectricityDeliveryFirmSub


class ElectricityDeliveryPointSub(supermod.ElectricityDeliveryPoint):
    def __init__(self, deliveryPointScheme=None, valueOf_=None):
        super(ElectricityDeliveryPointSub, self).__init__(deliveryPointScheme, valueOf_, )
supermod.ElectricityDeliveryPoint.subclass = ElectricityDeliveryPointSub
# end class ElectricityDeliveryPointSub


class ElectricityDeliverySystemFirmSub(supermod.ElectricityDeliverySystemFirm):
    def __init__(self, applicable=None, system=None):
        super(ElectricityDeliverySystemFirmSub, self).__init__(applicable, system, )
supermod.ElectricityDeliverySystemFirm.subclass = ElectricityDeliverySystemFirmSub
# end class ElectricityDeliverySystemFirmSub


class ElectricityDeliveryTypeSub(supermod.ElectricityDeliveryType):
    def __init__(self, firm=None, nonFirm=None, systemFirm=None, unitFirm=None):
        super(ElectricityDeliveryTypeSub, self).__init__(firm, nonFirm, systemFirm, unitFirm, )
supermod.ElectricityDeliveryType.subclass = ElectricityDeliveryTypeSub
# end class ElectricityDeliveryTypeSub


class ElectricityDeliveryUnitFirmSub(supermod.ElectricityDeliveryUnitFirm):
    def __init__(self, applicable=None, generationAsset=None):
        super(ElectricityDeliveryUnitFirmSub, self).__init__(applicable, generationAsset, )
supermod.ElectricityDeliveryUnitFirm.subclass = ElectricityDeliveryUnitFirmSub
# end class ElectricityDeliveryUnitFirmSub


class ElectricityPhysicalDeliveryQuantitySub(supermod.ElectricityPhysicalDeliveryQuantity):
    def __init__(self, id=None, quantityUnit=None, quantityFrequency=None, quantity=None, settlementPeriodsReference=None):
        super(ElectricityPhysicalDeliveryQuantitySub, self).__init__(id, quantityUnit, quantityFrequency, quantity, settlementPeriodsReference, )
supermod.ElectricityPhysicalDeliveryQuantity.subclass = ElectricityPhysicalDeliveryQuantitySub
# end class ElectricityPhysicalDeliveryQuantitySub


class ElectricityPhysicalDeliveryQuantityScheduleSub(supermod.ElectricityPhysicalDeliveryQuantitySchedule):
    def __init__(self, id=None, quantityStep=None, deliveryPeriodsReference=None, deliveryPeriodsScheduleReference=None, settlementPeriodsReference=None):
        super(ElectricityPhysicalDeliveryQuantityScheduleSub, self).__init__(id, quantityStep, deliveryPeriodsReference, deliveryPeriodsScheduleReference, settlementPeriodsReference, )
supermod.ElectricityPhysicalDeliveryQuantitySchedule.subclass = ElectricityPhysicalDeliveryQuantityScheduleSub
# end class ElectricityPhysicalDeliveryQuantityScheduleSub


class ElectricityPhysicalQuantitySub(supermod.ElectricityPhysicalQuantity):
    def __init__(self, id=None, physicalQuantity=None, physicalQuantitySchedule=None, totalPhysicalQuantity=None):
        super(ElectricityPhysicalQuantitySub, self).__init__(id, physicalQuantity, physicalQuantitySchedule, totalPhysicalQuantity, )
supermod.ElectricityPhysicalQuantity.subclass = ElectricityPhysicalQuantitySub
# end class ElectricityPhysicalQuantitySub


class ElectricityProductSub(supermod.ElectricityProduct):
    def __init__(self, type_=None, voltage=None):
        super(ElectricityProductSub, self).__init__(type_, voltage, )
supermod.ElectricityProduct.subclass = ElectricityProductSub
# end class ElectricityProductSub


class ElectricityTransmissionContingencySub(supermod.ElectricityTransmissionContingency):
    def __init__(self, contingency=None, contingentParty=None):
        super(ElectricityTransmissionContingencySub, self).__init__(contingency, contingentParty, )
supermod.ElectricityTransmissionContingency.subclass = ElectricityTransmissionContingencySub
# end class ElectricityTransmissionContingencySub


class ElectricityTransmissionContingencyTypeSub(supermod.ElectricityTransmissionContingencyType):
    def __init__(self, electricityTransmissionContingencyScheme='http://www.fpml.org/coding-scheme/electricity-transmission-contingency', valueOf_=None):
        super(ElectricityTransmissionContingencyTypeSub, self).__init__(electricityTransmissionContingencyScheme, valueOf_, )
supermod.ElectricityTransmissionContingencyType.subclass = ElectricityTransmissionContingencyTypeSub
# end class ElectricityTransmissionContingencyTypeSub


class EnvironmentalProductSub(supermod.EnvironmentalProduct):
    def __init__(self, productType=None, compliancePeriod=None, vintage=None, applicableLaw=None, trackingSystem=None):
        super(EnvironmentalProductSub, self).__init__(productType, compliancePeriod, vintage, applicableLaw, trackingSystem, )
supermod.EnvironmentalProduct.subclass = EnvironmentalProductSub
# end class EnvironmentalProductSub


class EnvironmentalProductApplicableLawSub(supermod.EnvironmentalProductApplicableLaw):
    def __init__(self, environmentalProductApplicableLawScheme='http://www.fpml.org/coding-scheme/governing-law', valueOf_=None):
        super(EnvironmentalProductApplicableLawSub, self).__init__(environmentalProductApplicableLawScheme, valueOf_, )
supermod.EnvironmentalProductApplicableLaw.subclass = EnvironmentalProductApplicableLawSub
# end class EnvironmentalProductApplicableLawSub


class EnvironmentalProductComplaincePeriodSub(supermod.EnvironmentalProductComplaincePeriod):
    def __init__(self, startYear=None, endYear=None):
        super(EnvironmentalProductComplaincePeriodSub, self).__init__(startYear, endYear, )
supermod.EnvironmentalProductComplaincePeriod.subclass = EnvironmentalProductComplaincePeriodSub
# end class EnvironmentalProductComplaincePeriodSub


class EnvironmentalTrackingSystemSub(supermod.EnvironmentalTrackingSystem):
    def __init__(self, commodityEnvironmentalTrackingSystemScheme='http://www.fpml.org/coding-scheme/commodity-environmental-tracking-system', valueOf_=None):
        super(EnvironmentalTrackingSystemSub, self).__init__(commodityEnvironmentalTrackingSystemScheme, valueOf_, )
supermod.EnvironmentalTrackingSystem.subclass = EnvironmentalTrackingSystemSub
# end class EnvironmentalTrackingSystemSub


class FinancialSwapLegSub(supermod.FinancialSwapLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, extensiontype_=None):
        super(FinancialSwapLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, extensiontype_, )
supermod.FinancialSwapLeg.subclass = FinancialSwapLegSub
# end class FinancialSwapLegSub


class FixedPriceSub(supermod.FixedPrice):
    def __init__(self, id=None, price=None, priceCurrency=None, priceUnit=None, extensiontype_=None):
        super(FixedPriceSub, self).__init__(id, price, priceCurrency, priceUnit, extensiontype_, )
supermod.FixedPrice.subclass = FixedPriceSub
# end class FixedPriceSub


class FixedPriceLegSub(supermod.FixedPriceLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, calculationDates=None, calculationPeriods=None, calculationPeriodsSchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, fixedPriceSchedule=None, fixedPrice=None, worldscaleRate=None, contractRate=None, settlementPeriodsPrice=None, totalPrice=None, notionalQuantitySchedule=None, notionalQuantity=None, settlementPeriodsNotionalQuantity=None, totalNotionalQuantity=None, quantityReference=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None, flatRate=None, flatRateAmount=None):
        super(FixedPriceLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, calculationDates, calculationPeriods, calculationPeriodsSchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, fixedPriceSchedule, fixedPrice, worldscaleRate, contractRate, settlementPeriodsPrice, totalPrice, notionalQuantitySchedule, notionalQuantity, settlementPeriodsNotionalQuantity, totalNotionalQuantity, quantityReference, relativePaymentDates, paymentDates, masterAgreementPaymentDates, flatRate, flatRateAmount, )
supermod.FixedPriceLeg.subclass = FixedPriceLegSub
# end class FixedPriceLegSub


class FloatingLegCalculationSub(supermod.FloatingLegCalculation):
    def __init__(self, pricingDates=None, averagingMethod=None, conversionFactor=None, rounding=None, spread=None, spreadSchedule=None, spreadPercentage=None, fx=None, extensiontype_=None):
        super(FloatingLegCalculationSub, self).__init__(pricingDates, averagingMethod, conversionFactor, rounding, spread, spreadSchedule, spreadPercentage, fx, extensiontype_, )
supermod.FloatingLegCalculation.subclass = FloatingLegCalculationSub
# end class FloatingLegCalculationSub


class FloatingPriceLegSub(supermod.FloatingPriceLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, calculationDates=None, calculationPeriods=None, calculationPeriodsSchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, commodity=None, notionalQuantitySchedule=None, notionalQuantity=None, settlementPeriodsNotionalQuantity=None, totalNotionalQuantity=None, quantityReference=None, calculation=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None, flatRate=None, flatRateAmount=None):
        super(FloatingPriceLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, calculationDates, calculationPeriods, calculationPeriodsSchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, commodity, notionalQuantitySchedule, notionalQuantity, settlementPeriodsNotionalQuantity, totalNotionalQuantity, quantityReference, calculation, relativePaymentDates, paymentDates, masterAgreementPaymentDates, flatRate, flatRateAmount, )
supermod.FloatingPriceLeg.subclass = FloatingPriceLegSub
# end class FloatingPriceLegSub


class FloatingStrikePriceSub(supermod.FloatingStrikePrice):
    def __init__(self, pricingDates=None, averagingMethod=None, conversionFactor=None, rounding=None, spread=None, spreadSchedule=None, spreadPercentage=None, fx=None, commodity=None):
        super(FloatingStrikePriceSub, self).__init__(pricingDates, averagingMethod, conversionFactor, rounding, spread, spreadSchedule, spreadPercentage, fx, commodity, )
supermod.FloatingStrikePrice.subclass = FloatingStrikePriceSub
# end class FloatingStrikePriceSub


class GasDeliverySub(supermod.GasDelivery):
    def __init__(self, deliveryPoint=None, entryPoint=None, withdrawalPoint=None, deliveryType=None, interconnectionPoint=None, buyerHub=None, sellerHub=None):
        super(GasDeliverySub, self).__init__(deliveryPoint, entryPoint, withdrawalPoint, deliveryType, interconnectionPoint, buyerHub, sellerHub, )
supermod.GasDelivery.subclass = GasDeliverySub
# end class GasDeliverySub


class GasDeliveryPeriodsSub(supermod.GasDeliveryPeriods):
    def __init__(self, id=None, periods=None, periodsSchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, supplyStartTime=None, supplyEndTime=None):
        super(GasDeliveryPeriodsSub, self).__init__(id, periods, periodsSchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, supplyStartTime, supplyEndTime, )
supermod.GasDeliveryPeriods.subclass = GasDeliveryPeriodsSub
# end class GasDeliveryPeriodsSub


class GasDeliveryPointSub(supermod.GasDeliveryPoint):
    def __init__(self, deliveryPointScheme=None, valueOf_=None):
        super(GasDeliveryPointSub, self).__init__(deliveryPointScheme, valueOf_, )
supermod.GasDeliveryPoint.subclass = GasDeliveryPointSub
# end class GasDeliveryPointSub


class GasPhysicalQuantitySub(supermod.GasPhysicalQuantity):
    def __init__(self, id=None, physicalQuantity=None, physicalQuantitySchedule=None, totalPhysicalQuantity=None, minPhysicalQuantity=None, maxPhysicalQuantity=None, electingParty=None):
        super(GasPhysicalQuantitySub, self).__init__(id, physicalQuantity, physicalQuantitySchedule, totalPhysicalQuantity, minPhysicalQuantity, maxPhysicalQuantity, electingParty, )
supermod.GasPhysicalQuantity.subclass = GasPhysicalQuantitySub
# end class GasPhysicalQuantitySub


class GasProductSub(supermod.GasProduct):
    def __init__(self, type_=None, calorificValue=None, quality=None):
        super(GasProductSub, self).__init__(type_, calorificValue, quality, )
supermod.GasProduct.subclass = GasProductSub
# end class GasProductSub


class GasQualitySub(supermod.GasQuality):
    def __init__(self, gasQualityScheme='http://www.fpml.org/coding-scheme/commodity-gas-quality', valueOf_=None):
        super(GasQualitySub, self).__init__(gasQualityScheme, valueOf_, )
supermod.GasQuality.subclass = GasQualitySub
# end class GasQualitySub


class InterconnectionPointSub(supermod.InterconnectionPoint):
    def __init__(self, interconnectionPointScheme='http://www.fpml.org/coding-scheme/external/eic-codes', valueOf_=None):
        super(InterconnectionPointSub, self).__init__(interconnectionPointScheme, valueOf_, )
supermod.InterconnectionPoint.subclass = InterconnectionPointSub
# end class InterconnectionPointSub


class LagSub(supermod.Lag):
    def __init__(self, id=None, lagDuration=None, firstObservationDateOffset=None):
        super(LagSub, self).__init__(id, lagDuration, firstObservationDateOffset, )
supermod.Lag.subclass = LagSub
# end class LagSub


class LagReferenceSub(supermod.LagReference):
    def __init__(self, href=None):
        super(LagReferenceSub, self).__init__(href, )
supermod.LagReference.subclass = LagReferenceSub
# end class LagReferenceSub


class MarketDisruptionEventSub(supermod.MarketDisruptionEvent):
    def __init__(self, commodityMarketDisruptionScheme='http://www.fpml.org/coding-scheme/commodity-market-disruption', valueOf_=None):
        super(MarketDisruptionEventSub, self).__init__(commodityMarketDisruptionScheme, valueOf_, )
supermod.MarketDisruptionEvent.subclass = MarketDisruptionEventSub
# end class MarketDisruptionEventSub


class MaterialSub(supermod.Material):
    def __init__(self, commodityMetalProductTypeScheme='http://www.fpml.org/coding-scheme/commodity-metal-product-type', valueOf_=None):
        super(MaterialSub, self).__init__(commodityMetalProductTypeScheme, valueOf_, )
supermod.Material.subclass = MaterialSub
# end class MaterialSub


class MetalSub(supermod.Metal):
    def __init__(self, material=None, shape=None, brand=None, grade=None):
        super(MetalSub, self).__init__(material, shape, brand, grade, )
supermod.Metal.subclass = MetalSub
# end class MetalSub


class MetalDeliverySub(supermod.MetalDelivery):
    def __init__(self, deliveryLocation=None, risk=None, totalQuantityTolerance=None, periodQuantityTolerance=None, title=None):
        super(MetalDeliverySub, self).__init__(deliveryLocation, risk, totalQuantityTolerance, periodQuantityTolerance, title, )
supermod.MetalDelivery.subclass = MetalDeliverySub
# end class MetalDeliverySub


class NonPeriodicFixedPriceLegSub(supermod.NonPeriodicFixedPriceLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, fixedPrice=None, totalPrice=None, quantityReference=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None):
        super(NonPeriodicFixedPriceLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, fixedPrice, totalPrice, quantityReference, relativePaymentDates, paymentDates, masterAgreementPaymentDates, )
supermod.NonPeriodicFixedPriceLeg.subclass = NonPeriodicFixedPriceLegSub
# end class NonPeriodicFixedPriceLegSub


class OilDeliverySub(supermod.OilDelivery):
    def __init__(self, pipeline=None, transfer=None, importerOfRecord=None, absoluteTolerance=None, percentageTolerance=None):
        super(OilDeliverySub, self).__init__(pipeline, transfer, importerOfRecord, absoluteTolerance, percentageTolerance, )
supermod.OilDelivery.subclass = OilDeliverySub
# end class OilDeliverySub


class OilPipelineDeliverySub(supermod.OilPipelineDelivery):
    def __init__(self, pipelineName=None, withdrawalPoint=None, entryPoint=None, deliverableByBarge=None, risk=None, cycle=None):
        super(OilPipelineDeliverySub, self).__init__(pipelineName, withdrawalPoint, entryPoint, deliverableByBarge, risk, cycle, )
supermod.OilPipelineDelivery.subclass = OilPipelineDeliverySub
# end class OilPipelineDeliverySub


class OilProductSub(supermod.OilProduct):
    def __init__(self, type_=None, grade=None):
        super(OilProductSub, self).__init__(type_, grade, )
supermod.OilProduct.subclass = OilProductSub
# end class OilProductSub


class OilProductTypeSub(supermod.OilProductType):
    def __init__(self, commodityOilProductTypeScheme='http://www.fpml.org/coding-scheme/commodity-oil-product-type', valueOf_=None):
        super(OilProductTypeSub, self).__init__(commodityOilProductTypeScheme, valueOf_, )
supermod.OilProductType.subclass = OilProductTypeSub
# end class OilProductTypeSub


class OilTransferDeliverySub(supermod.OilTransferDelivery):
    def __init__(self, applicable=None, deliveryLocation=None):
        super(OilTransferDeliverySub, self).__init__(applicable, deliveryLocation, )
supermod.OilTransferDelivery.subclass = OilTransferDeliverySub
# end class OilTransferDeliverySub


class PercentageToleranceSub(supermod.PercentageTolerance):
    def __init__(self, postitive=None, negative=None, option=None):
        super(PercentageToleranceSub, self).__init__(postitive, negative, option, )
supermod.PercentageTolerance.subclass = PercentageToleranceSub
# end class PercentageToleranceSub


class PhysicalForwardLegSub(supermod.PhysicalForwardLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, extensiontype_=None):
        super(PhysicalForwardLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, extensiontype_, )
supermod.PhysicalForwardLeg.subclass = PhysicalForwardLegSub
# end class PhysicalForwardLegSub


class PhysicalSwapLegSub(supermod.PhysicalSwapLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, extensiontype_=None):
        super(PhysicalSwapLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, extensiontype_, )
supermod.PhysicalSwapLeg.subclass = PhysicalSwapLegSub
# end class PhysicalSwapLegSub


class QuantityReferenceSub(supermod.QuantityReference):
    def __init__(self, href=None):
        super(QuantityReferenceSub, self).__init__(href, )
supermod.QuantityReference.subclass = QuantityReferenceSub
# end class QuantityReferenceSub


class ReferenceLevelSub(supermod.ReferenceLevel):
    def __init__(self, amount=None, referenceLevelUnit=None):
        super(ReferenceLevelSub, self).__init__(amount, referenceLevelUnit, )
supermod.ReferenceLevel.subclass = ReferenceLevelSub
# end class ReferenceLevelSub


class ReferenceLevelUnitSub(supermod.ReferenceLevelUnit):
    def __init__(self, weatherIndexReferenceLevelScheme='http://www.fpml.org/coding-scheme/weather-index-reference-level', valueOf_=None):
        super(ReferenceLevelUnitSub, self).__init__(weatherIndexReferenceLevelScheme, valueOf_, )
supermod.ReferenceLevelUnit.subclass = ReferenceLevelUnitSub
# end class ReferenceLevelUnitSub


class SequencedDisruptionFallbackSub(supermod.SequencedDisruptionFallback):
    def __init__(self, fallback=None, sequence=None):
        super(SequencedDisruptionFallbackSub, self).__init__(fallback, sequence, )
supermod.SequencedDisruptionFallback.subclass = SequencedDisruptionFallbackSub
# end class SequencedDisruptionFallbackSub


class SettlementPeriodsSub(supermod.SettlementPeriods):
    def __init__(self, id=None, duration=None, applicableDay=None, startTime=None, endTime=None, excludeHolidays=None, includeHolidays=None):
        super(SettlementPeriodsSub, self).__init__(id, duration, applicableDay, startTime, endTime, excludeHolidays, includeHolidays, )
supermod.SettlementPeriods.subclass = SettlementPeriodsSub
# end class SettlementPeriodsSub


class SettlementPeriodsFixedPriceSub(supermod.SettlementPeriodsFixedPrice):
    def __init__(self, id=None, price=None, priceCurrency=None, priceUnit=None, settlementPeriodsReference=None):
        super(SettlementPeriodsFixedPriceSub, self).__init__(id, price, priceCurrency, priceUnit, settlementPeriodsReference, )
supermod.SettlementPeriodsFixedPrice.subclass = SettlementPeriodsFixedPriceSub
# end class SettlementPeriodsFixedPriceSub


class SettlementPeriodsReferenceSub(supermod.SettlementPeriodsReference):
    def __init__(self, href=None):
        super(SettlementPeriodsReferenceSub, self).__init__(href, )
supermod.SettlementPeriodsReference.subclass = SettlementPeriodsReferenceSub
# end class SettlementPeriodsReferenceSub


class SettlementPeriodsScheduleSub(supermod.SettlementPeriodsSchedule):
    def __init__(self, settlementPeriodsStep=None, deliveryPeriodsReference=None, deliveryPeriodsScheduleReference=None):
        super(SettlementPeriodsScheduleSub, self).__init__(settlementPeriodsStep, deliveryPeriodsReference, deliveryPeriodsScheduleReference, )
supermod.SettlementPeriodsSchedule.subclass = SettlementPeriodsScheduleSub
# end class SettlementPeriodsScheduleSub


class SettlementPeriodsStepSub(supermod.SettlementPeriodsStep):
    def __init__(self, settlementPeriodsReference=None):
        super(SettlementPeriodsStepSub, self).__init__(settlementPeriodsReference, )
supermod.SettlementPeriodsStep.subclass = SettlementPeriodsStepSub
# end class SettlementPeriodsStepSub


class StrikePriceBasketReferenceSub(supermod.StrikePriceBasketReference):
    def __init__(self, href=None):
        super(StrikePriceBasketReferenceSub, self).__init__(href, )
supermod.StrikePriceBasketReference.subclass = StrikePriceBasketReferenceSub
# end class StrikePriceBasketReferenceSub


class StrikePriceUnderlyingReferenceSub(supermod.StrikePriceUnderlyingReference):
    def __init__(self, href=None):
        super(StrikePriceUnderlyingReferenceSub, self).__init__(href, )
supermod.StrikePriceUnderlyingReference.subclass = StrikePriceUnderlyingReferenceSub
# end class StrikePriceUnderlyingReferenceSub


class UnitQuantitySub(supermod.UnitQuantity):
    def __init__(self, id=None, quantityUnit=None, quantity=None):
        super(UnitQuantitySub, self).__init__(id, quantityUnit, quantity, )
supermod.UnitQuantity.subclass = UnitQuantitySub
# end class UnitQuantitySub


class WeatherCalculationPeriodSub(supermod.WeatherCalculationPeriod):
    def __init__(self, calculationPeriodFirstDay=None, calculationPeriodEndDay=None):
        super(WeatherCalculationPeriodSub, self).__init__(calculationPeriodFirstDay, calculationPeriodEndDay, )
supermod.WeatherCalculationPeriod.subclass = WeatherCalculationPeriodSub
# end class WeatherCalculationPeriodSub


class WeatherCalculationPeriodsSub(supermod.WeatherCalculationPeriods):
    def __init__(self, id=None, calculationPeriod=None):
        super(WeatherCalculationPeriodsSub, self).__init__(id, calculationPeriod, )
supermod.WeatherCalculationPeriods.subclass = WeatherCalculationPeriodsSub
# end class WeatherCalculationPeriodsSub


class WeatherIndexSub(supermod.WeatherIndex):
    def __init__(self, id=None, quantity=None, unit=None):
        super(WeatherIndexSub, self).__init__(id, quantity, unit, )
supermod.WeatherIndex.subclass = WeatherIndexSub
# end class WeatherIndexSub


class WeatherIndexDataSub(supermod.WeatherIndexData):
    def __init__(self, referenceLevel=None, dataProvider=None, finalEditedData=None, weatherStation=None, weatherStationFallback=None, weatherStationSecondFallback=None, alternativeDataProvider=None, synopticDataFallback=None, adjustmentToFallbackWeatherStation=None, primaryDisruptionFallbacks=None, secondaryDisruptionFallbacks=None):
        super(WeatherIndexDataSub, self).__init__(referenceLevel, dataProvider, finalEditedData, weatherStation, weatherStationFallback, weatherStationSecondFallback, alternativeDataProvider, synopticDataFallback, adjustmentToFallbackWeatherStation, primaryDisruptionFallbacks, secondaryDisruptionFallbacks, )
supermod.WeatherIndexData.subclass = WeatherIndexDataSub
# end class WeatherIndexDataSub


class WeatherLegSub(supermod.WeatherLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, weatherIndexLevel=None, weatherCalculationPeriods=None, weatherCalculationPeriodsReference=None, weatherNotionalAmount=None, calculation=None, paymentDates=None, weatherIndexData=None):
        super(WeatherLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, weatherIndexLevel, weatherCalculationPeriods, weatherCalculationPeriodsReference, weatherNotionalAmount, calculation, paymentDates, weatherIndexData, )
supermod.WeatherLeg.subclass = WeatherLegSub
# end class WeatherLegSub


class WeatherLegCalculationSub(supermod.WeatherLegCalculation):
    def __init__(self, settlementLevel=None, referenceLevelEqualsZero=None, calculationDate=None, businessDays=None, dataCorrection=None, correctionPeriod=None, maximumPaymentAmount=None, maximumTransactionPaymentAmount=None, rounding=None):
        super(WeatherLegCalculationSub, self).__init__(settlementLevel, referenceLevelEqualsZero, calculationDate, businessDays, dataCorrection, correctionPeriod, maximumPaymentAmount, maximumTransactionPaymentAmount, rounding, )
supermod.WeatherLegCalculation.subclass = WeatherLegCalculationSub
# end class WeatherLegCalculationSub


class WeatherStationSub(supermod.WeatherStation):
    def __init__(self, weatherStationCity=None, weatherStationAirport=None, weatherStationWBAN=None, weatherStationWMO=None):
        super(WeatherStationSub, self).__init__(weatherStationCity, weatherStationAirport, weatherStationWBAN, weatherStationWMO, )
supermod.WeatherStation.subclass = WeatherStationSub
# end class WeatherStationSub


class WeatherStationAirportSub(supermod.WeatherStationAirport):
    def __init__(self, weatherStationAirportScheme='http://www.fpml.org/coding-scheme/external/weather-station-airport', id=None, valueOf_=None):
        super(WeatherStationAirportSub, self).__init__(weatherStationAirportScheme, id, valueOf_, )
supermod.WeatherStationAirport.subclass = WeatherStationAirportSub
# end class WeatherStationAirportSub


class WeatherStationWBANSub(supermod.WeatherStationWBAN):
    def __init__(self, weatherStationWBANScheme='http://www.fpml.org/coding-scheme/external/weather-station-wban', id=None, valueOf_=None):
        super(WeatherStationWBANSub, self).__init__(weatherStationWBANScheme, id, valueOf_, )
supermod.WeatherStationWBAN.subclass = WeatherStationWBANSub
# end class WeatherStationWBANSub


class WeatherStationWMOSub(supermod.WeatherStationWMO):
    def __init__(self, weatherStationWMOScheme='http://www.fpml.org/coding-scheme/external/weather-station-wmo', id=None, valueOf_=None):
        super(WeatherStationWMOSub, self).__init__(weatherStationWMOScheme, id, valueOf_, )
supermod.WeatherStationWMO.subclass = WeatherStationWMOSub
# end class WeatherStationWMOSub


class AsianSub(supermod.Asian):
    def __init__(self, averagingInOut=None, strikeFactor=None, averagingPeriodIn=None, averagingPeriodOut=None):
        super(AsianSub, self).__init__(averagingInOut, strikeFactor, averagingPeriodIn, averagingPeriodOut, )
supermod.Asian.subclass = AsianSub
# end class AsianSub


class AveragingObservationListSub(supermod.AveragingObservationList):
    def __init__(self, averagingObservation=None):
        super(AveragingObservationListSub, self).__init__(averagingObservation, )
supermod.AveragingObservationList.subclass = AveragingObservationListSub
# end class AveragingObservationListSub


class AveragingPeriodSub(supermod.AveragingPeriod):
    def __init__(self, schedule=None, averagingDateTimes=None, averagingObservations=None, marketDisruption=None):
        super(AveragingPeriodSub, self).__init__(schedule, averagingDateTimes, averagingObservations, marketDisruption, )
supermod.AveragingPeriod.subclass = AveragingPeriodSub
# end class AveragingPeriodSub


class AveragingScheduleSub(supermod.AveragingSchedule):
    def __init__(self, startDate=None, endDate=None, averagingPeriodFrequency=None):
        super(AveragingScheduleSub, self).__init__(startDate, endDate, averagingPeriodFrequency, )
supermod.AveragingSchedule.subclass = AveragingScheduleSub
# end class AveragingScheduleSub


class BarrierSub(supermod.Barrier):
    def __init__(self, barrierCap=None, barrierFloor=None):
        super(BarrierSub, self).__init__(barrierCap, barrierFloor, )
supermod.Barrier.subclass = BarrierSub
# end class BarrierSub


class CalendarSpreadSub(supermod.CalendarSpread):
    def __init__(self, expirationDateTwo=None):
        super(CalendarSpreadSub, self).__init__(expirationDateTwo, )
supermod.CalendarSpread.subclass = CalendarSpreadSub
# end class CalendarSpreadSub


class CompositeSub(supermod.Composite):
    def __init__(self, determinationMethod=None, relativeDate=None, fxSpotRateSource=None):
        super(CompositeSub, self).__init__(determinationMethod, relativeDate, fxSpotRateSource, )
supermod.Composite.subclass = CompositeSub
# end class CompositeSub


class CreditEventNoticeSub(supermod.CreditEventNotice):
    def __init__(self, notifyingParty=None, businessCenter=None, publiclyAvailableInformation=None):
        super(CreditEventNoticeSub, self).__init__(notifyingParty, businessCenter, publiclyAvailableInformation, )
supermod.CreditEventNotice.subclass = CreditEventNoticeSub
# end class CreditEventNoticeSub


class CreditEventsSub(supermod.CreditEvents):
    def __init__(self, id=None, bankruptcy=None, failureToPay=None, failureToPayPrincipal=None, failureToPayInterest=None, obligationDefault=None, obligationAcceleration=None, repudiationMoratorium=None, restructuring=None, governmentalIntervention=None, distressedRatingsDowngrade=None, maturityExtension=None, writedown=None, impliedWritedown=None, defaultRequirement=None, creditEventNotice=None):
        super(CreditEventsSub, self).__init__(id, bankruptcy, failureToPay, failureToPayPrincipal, failureToPayInterest, obligationDefault, obligationAcceleration, repudiationMoratorium, restructuring, governmentalIntervention, distressedRatingsDowngrade, maturityExtension, writedown, impliedWritedown, defaultRequirement, creditEventNotice, )
supermod.CreditEvents.subclass = CreditEventsSub
# end class CreditEventsSub


class CreditEventsReferenceSub(supermod.CreditEventsReference):
    def __init__(self, href=None):
        super(CreditEventsReferenceSub, self).__init__(href, )
supermod.CreditEventsReference.subclass = CreditEventsReferenceSub
# end class CreditEventsReferenceSub


class FailureToPaySub(supermod.FailureToPay):
    def __init__(self, applicable=None, gracePeriodExtension=None, paymentRequirement=None):
        super(FailureToPaySub, self).__init__(applicable, gracePeriodExtension, paymentRequirement, )
supermod.FailureToPay.subclass = FailureToPaySub
# end class FailureToPaySub


class FeaturePaymentSub(supermod.FeaturePayment):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, levelPercentage=None, amount=None, time=None, currency=None, featurePaymentDate=None):
        super(FeaturePaymentSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, levelPercentage, amount, time, currency, featurePaymentDate, )
supermod.FeaturePayment.subclass = FeaturePaymentSub
# end class FeaturePaymentSub


class FxFeatureSub(supermod.FxFeature):
    def __init__(self, referenceCurrency=None, composite=None, quanto=None, crossCurrency=None):
        super(FxFeatureSub, self).__init__(referenceCurrency, composite, quanto, crossCurrency, )
supermod.FxFeature.subclass = FxFeatureSub
# end class FxFeatureSub


class GracePeriodExtensionSub(supermod.GracePeriodExtension):
    def __init__(self, applicable=None, gracePeriod=None):
        super(GracePeriodExtensionSub, self).__init__(applicable, gracePeriod, )
supermod.GracePeriodExtension.subclass = GracePeriodExtensionSub
# end class GracePeriodExtensionSub


class KnockSub(supermod.Knock):
    def __init__(self, knockIn=None, knockOut=None):
        super(KnockSub, self).__init__(knockIn, knockOut, )
supermod.Knock.subclass = KnockSub
# end class KnockSub


class MarketDisruptionSub(supermod.MarketDisruption):
    def __init__(self, marketDisruptionScheme='http://www.fpml.org/coding-scheme/market-disruption', valueOf_=None):
        super(MarketDisruptionSub, self).__init__(marketDisruptionScheme, valueOf_, )
supermod.MarketDisruption.subclass = MarketDisruptionSub
# end class MarketDisruptionSub


class NotifyingPartySub(supermod.NotifyingParty):
    def __init__(self, buyerPartyReference=None, sellerPartyReference=None):
        super(NotifyingPartySub, self).__init__(buyerPartyReference, sellerPartyReference, )
supermod.NotifyingParty.subclass = NotifyingPartySub
# end class NotifyingPartySub


class OptionSub(supermod.Option):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, extensiontype_=None):
        super(OptionSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, extensiontype_, )
supermod.Option.subclass = OptionSub
# end class OptionSub


class OptionBaseSub(supermod.OptionBase):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, optionType=None, extensiontype_=None):
        super(OptionBaseSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, optionType, extensiontype_, )
supermod.OptionBase.subclass = OptionBaseSub
# end class OptionBaseSub


class OptionBaseExtendedSub(supermod.OptionBaseExtended):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, optionType=None, premium=None, exercise=None, exerciseProcedure=None, feature=None, notionalReference=None, notionalAmount=None, optionEntitlement=None, entitlementCurrency=None, numberOfOptions=None, settlementType=None, settlementDate=None, settlementAmount=None, settlementCurrency=None):
        super(OptionBaseExtendedSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, optionType, premium, exercise, exerciseProcedure, feature, notionalReference, notionalAmount, optionEntitlement, entitlementCurrency, numberOfOptions, settlementType, settlementDate, settlementAmount, settlementCurrency, )
supermod.OptionBaseExtended.subclass = OptionBaseExtendedSub
# end class OptionBaseExtendedSub


class OptionFeatureSub(supermod.OptionFeature):
    def __init__(self, fxFeature=None, strategyFeature=None, asian=None, barrier=None, knock=None, passThrough=None):
        super(OptionFeatureSub, self).__init__(fxFeature, strategyFeature, asian, barrier, knock, passThrough, )
supermod.OptionFeature.subclass = OptionFeatureSub
# end class OptionFeatureSub


class OptionNumericStrikeSub(supermod.OptionNumericStrike):
    def __init__(self, strikePrice=None, strikePercentage=None, extensiontype_=None):
        super(OptionNumericStrikeSub, self).__init__(strikePrice, strikePercentage, extensiontype_, )
supermod.OptionNumericStrike.subclass = OptionNumericStrikeSub
# end class OptionNumericStrikeSub


class OptionStrikeSub(supermod.OptionStrike):
    def __init__(self, strikePrice=None, strikePercentage=None, currency=None):
        super(OptionStrikeSub, self).__init__(strikePrice, strikePercentage, currency, )
supermod.OptionStrike.subclass = OptionStrikeSub
# end class OptionStrikeSub


class PassThroughSub(supermod.PassThrough):
    def __init__(self, passThroughItem=None):
        super(PassThroughSub, self).__init__(passThroughItem, )
supermod.PassThrough.subclass = PassThroughSub
# end class PassThroughSub


class PassThroughItemSub(supermod.PassThroughItem):
    def __init__(self, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, underlyerReference=None, passThroughPercentage=None):
        super(PassThroughItemSub, self).__init__(payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, underlyerReference, passThroughPercentage, )
supermod.PassThroughItem.subclass = PassThroughItemSub
# end class PassThroughItemSub


class PremiumSub(supermod.Premium):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentAmount=None, paymentDate=None, premiumType=None, pricePerOption=None, percentageOfNotional=None, discountFactor=None, presentValueAmount=None):
        super(PremiumSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentAmount, paymentDate, premiumType, pricePerOption, percentageOfNotional, discountFactor, presentValueAmount, )
supermod.Premium.subclass = PremiumSub
# end class PremiumSub


class PubliclyAvailableInformationSub(supermod.PubliclyAvailableInformation):
    def __init__(self, standardPublicSources=None, publicSource=None, specifiedNumber=None):
        super(PubliclyAvailableInformationSub, self).__init__(standardPublicSources, publicSource, specifiedNumber, )
supermod.PubliclyAvailableInformation.subclass = PubliclyAvailableInformationSub
# end class PubliclyAvailableInformationSub


class QuantoSub(supermod.Quanto):
    def __init__(self, fxRate=None, fxSpotRateSource=None):
        super(QuantoSub, self).__init__(fxRate, fxSpotRateSource, )
supermod.Quanto.subclass = QuantoSub
# end class QuantoSub


class RestructuringSub(supermod.Restructuring):
    def __init__(self, applicable=None, restructuringType=None, multipleHolderObligation=None, multipleCreditEventNotices=None):
        super(RestructuringSub, self).__init__(applicable, restructuringType, multipleHolderObligation, multipleCreditEventNotices, )
supermod.Restructuring.subclass = RestructuringSub
# end class RestructuringSub


class RestructuringTypeSub(supermod.RestructuringType):
    def __init__(self, restructuringScheme='http://www.fpml.org/coding-scheme/restructuring', valueOf_=None):
        super(RestructuringTypeSub, self).__init__(restructuringScheme, valueOf_, )
supermod.RestructuringType.subclass = RestructuringTypeSub
# end class RestructuringTypeSub


class SettlementTermsSub(supermod.SettlementTerms):
    def __init__(self, id=None, settlementCurrency=None):
        super(SettlementTermsSub, self).__init__(id, settlementCurrency, )
supermod.SettlementTerms.subclass = SettlementTermsSub
# end class SettlementTermsSub


class StrategyFeatureSub(supermod.StrategyFeature):
    def __init__(self, strikeSpread=None, calendarSpread=None):
        super(StrategyFeatureSub, self).__init__(strikeSpread, calendarSpread, )
supermod.StrategyFeature.subclass = StrategyFeatureSub
# end class StrategyFeatureSub


class StrikeSpreadSub(supermod.StrikeSpread):
    def __init__(self, upperStrike=None, upperStrikeNumberOfOptions=None):
        super(StrikeSpreadSub, self).__init__(upperStrike, upperStrikeNumberOfOptions, )
supermod.StrikeSpread.subclass = StrikeSpreadSub
# end class StrikeSpreadSub


class TriggerSub(supermod.Trigger):
    def __init__(self, level=None, levelPercentage=None, creditEvents=None, creditEventsReference=None, triggerType=None, triggerTimeType=None):
        super(TriggerSub, self).__init__(level, levelPercentage, creditEvents, creditEventsReference, triggerType, triggerTimeType, )
supermod.Trigger.subclass = TriggerSub
# end class TriggerSub


class TriggerEventSub(supermod.TriggerEvent):
    def __init__(self, schedule=None, triggerDates=None, trigger=None, featurePayment=None):
        super(TriggerEventSub, self).__init__(schedule, triggerDates, trigger, featurePayment, )
supermod.TriggerEvent.subclass = TriggerEventSub
# end class TriggerEventSub


class WeightedAveragingObservationSub(supermod.WeightedAveragingObservation):
    def __init__(self, dateTime=None, observationNumber=None, weight=None):
        super(WeightedAveragingObservationSub, self).__init__(dateTime, observationNumber, weight, )
supermod.WeightedAveragingObservation.subclass = WeightedAveragingObservationSub
# end class WeightedAveragingObservationSub


class CrossRateSub(supermod.CrossRate):
    def __init__(self, currency1=None, currency2=None, quoteBasis=None, rate=None, spotRate=None, forwardPoints=None):
        super(CrossRateSub, self).__init__(currency1, currency2, quoteBasis, rate, spotRate, forwardPoints, )
supermod.CrossRate.subclass = CrossRateSub
# end class CrossRateSub


class CutNameSub(supermod.CutName):
    def __init__(self, cutNameScheme='http://www.fpml.org/coding-scheme/cut-name', valueOf_=None):
        super(CutNameSub, self).__init__(cutNameScheme, valueOf_, )
supermod.CutName.subclass = CutNameSub
# end class CutNameSub


class DualCurrencyFeatureSub(supermod.DualCurrencyFeature):
    def __init__(self, currency=None, fixingDate=None, fixingTime=None, strike=None, spotRate=None, interestAtRisk=None):
        super(DualCurrencyFeatureSub, self).__init__(currency, fixingDate, fixingTime, strike, spotRate, interestAtRisk, )
supermod.DualCurrencyFeature.subclass = DualCurrencyFeatureSub
# end class DualCurrencyFeatureSub


class DualCurrencyStrikePriceSub(supermod.DualCurrencyStrikePrice):
    def __init__(self, rate=None, strikeQuoteBasis=None):
        super(DualCurrencyStrikePriceSub, self).__init__(rate, strikeQuoteBasis, )
supermod.DualCurrencyStrikePrice.subclass = DualCurrencyStrikePriceSub
# end class DualCurrencyStrikePriceSub


class ExchangeRateSub(supermod.ExchangeRate):
    def __init__(self, quotedCurrencyPair=None, rate=None, spotRate=None, forwardPoints=None, pointValue=None, crossRate=None):
        super(ExchangeRateSub, self).__init__(quotedCurrencyPair, rate, spotRate, forwardPoints, pointValue, crossRate, )
supermod.ExchangeRate.subclass = ExchangeRateSub
# end class ExchangeRateSub


class FxAsianFeatureSub(supermod.FxAsianFeature):
    def __init__(self, primaryRateSource=None, secondaryRateSource=None, fixingTime=None, observationSchedule=None, rateObservation=None, rateObservationQuoteBasis=None, payoutFormula=None, precision=None):
        super(FxAsianFeatureSub, self).__init__(primaryRateSource, secondaryRateSource, fixingTime, observationSchedule, rateObservation, rateObservationQuoteBasis, payoutFormula, precision, )
supermod.FxAsianFeature.subclass = FxAsianFeatureSub
# end class FxAsianFeatureSub


class FxAverageRateObservationSub(supermod.FxAverageRateObservation):
    def __init__(self, date=None, averageRateWeightingFactor=None, rate=None):
        super(FxAverageRateObservationSub, self).__init__(date, averageRateWeightingFactor, rate, )
supermod.FxAverageRateObservation.subclass = FxAverageRateObservationSub
# end class FxAverageRateObservationSub


class FxAverageRateObservationScheduleSub(supermod.FxAverageRateObservationSchedule):
    def __init__(self, startDate=None, endDate=None, calculationPeriodFrequency=None):
        super(FxAverageRateObservationScheduleSub, self).__init__(startDate, endDate, calculationPeriodFrequency, )
supermod.FxAverageRateObservationSchedule.subclass = FxAverageRateObservationScheduleSub
# end class FxAverageRateObservationScheduleSub


class FxBarrierFeatureSub(supermod.FxBarrierFeature):
    def __init__(self, barrierType=None, direction=None, quotedCurrencyPair=None, triggerRate=None, informationSource=None, observationStartDate=None, observationStartTime=None, observationEndDate=None, observationEndTime=None, observationPoint=None):
        super(FxBarrierFeatureSub, self).__init__(barrierType, direction, quotedCurrencyPair, triggerRate, informationSource, observationStartDate, observationStartTime, observationEndDate, observationEndTime, observationPoint, )
supermod.FxBarrierFeature.subclass = FxBarrierFeatureSub
# end class FxBarrierFeatureSub


class FxBusinessCenterDateTimeSub(supermod.FxBusinessCenterDateTime):
    def __init__(self, date=None, time=None):
        super(FxBusinessCenterDateTimeSub, self).__init__(date, time, )
supermod.FxBusinessCenterDateTime.subclass = FxBusinessCenterDateTimeSub
# end class FxBusinessCenterDateTimeSub


class FxDigitalAmericanExerciseSub(supermod.FxDigitalAmericanExercise):
    def __init__(self, id=None, commencementDate=None, expiryDate=None, expiryTime=None, cutName=None, latestValueDate=None, extensiontype_=None):
        super(FxDigitalAmericanExerciseSub, self).__init__(id, commencementDate, expiryDate, expiryTime, cutName, latestValueDate, extensiontype_, )
supermod.FxDigitalAmericanExercise.subclass = FxDigitalAmericanExerciseSub
# end class FxDigitalAmericanExerciseSub


class FxDigitalOptionSub(supermod.FxDigitalOption):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, effectiveDate=None, tenorPeriod=None, americanExercise=None, touch=None, europeanExercise=None, trigger=None, exerciseProcedure=None, payout=None, premium=None):
        super(FxDigitalOptionSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, effectiveDate, tenorPeriod, americanExercise, touch, europeanExercise, trigger, exerciseProcedure, payout, premium, )
supermod.FxDigitalOption.subclass = FxDigitalOptionSub
# end class FxDigitalOptionSub


class FxDisruptionSub(supermod.FxDisruption):
    def __init__(self, baseCurrency=None, referenceCurrency=None, provisions=None):
        super(FxDisruptionSub, self).__init__(baseCurrency, referenceCurrency, provisions, )
supermod.FxDisruption.subclass = FxDisruptionSub
# end class FxDisruptionSub


class FxDisruptionEventSub(supermod.FxDisruptionEvent):
    def __init__(self, extensiontype_=None):
        super(FxDisruptionEventSub, self).__init__(extensiontype_, )
supermod.FxDisruptionEvent.subclass = FxDisruptionEventSub
# end class FxDisruptionEventSub


class FxDisruptionEventsSub(supermod.FxDisruptionEvents):
    def __init__(self, fxDisruptionEvent=None):
        super(FxDisruptionEventsSub, self).__init__(fxDisruptionEvent, )
supermod.FxDisruptionEvents.subclass = FxDisruptionEventsSub
# end class FxDisruptionEventsSub


class FxDisruptionFallbackSub(supermod.FxDisruptionFallback):
    def __init__(self, extensiontype_=None):
        super(FxDisruptionFallbackSub, self).__init__(extensiontype_, )
supermod.FxDisruptionFallback.subclass = FxDisruptionFallbackSub
# end class FxDisruptionFallbackSub


class FxDisruptionFallbacksSub(supermod.FxDisruptionFallbacks):
    def __init__(self, fxDisruptionFallback=None):
        super(FxDisruptionFallbacksSub, self).__init__(fxDisruptionFallback, )
supermod.FxDisruptionFallbacks.subclass = FxDisruptionFallbacksSub
# end class FxDisruptionFallbacksSub


class FxDisruptionProvisionsSub(supermod.FxDisruptionProvisions):
    def __init__(self, events=None, fallbacks=None, applicableTerms=None):
        super(FxDisruptionProvisionsSub, self).__init__(events, fallbacks, applicableTerms, )
supermod.FxDisruptionProvisions.subclass = FxDisruptionProvisionsSub
# end class FxDisruptionProvisionsSub


class FxEuropeanExerciseSub(supermod.FxEuropeanExercise):
    def __init__(self, id=None, expiryDate=None, expiryTime=None, cutName=None, valueDate=None):
        super(FxEuropeanExerciseSub, self).__init__(id, expiryDate, expiryTime, cutName, valueDate, )
supermod.FxEuropeanExercise.subclass = FxEuropeanExerciseSub
# end class FxEuropeanExerciseSub


class FxFallbackReferencePriceSub(supermod.FxFallbackReferencePrice):
    def __init__(self, primaryRateSource=None, secondaryRateSource=None):
        super(FxFallbackReferencePriceSub, self).__init__(primaryRateSource, secondaryRateSource, )
supermod.FxFallbackReferencePrice.subclass = FxFallbackReferencePriceSub
# end class FxFallbackReferencePriceSub


class FxFixingScheduleSimpleSub(supermod.FxFixingScheduleSimple):
    def __init__(self, startDate=None, endDate=None, dayType=None, businessCentersReference=None, businessCenters=None, fixingDate=None):
        super(FxFixingScheduleSimpleSub, self).__init__(startDate, endDate, dayType, businessCentersReference, businessCenters, fixingDate, )
supermod.FxFixingScheduleSimple.subclass = FxFixingScheduleSimpleSub
# end class FxFixingScheduleSimpleSub


class FxFlexibleForwardSub(supermod.FxFlexibleForward):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, putCurrency=None, callCurrency=None, notionalAmount=None, minimumExecutionAmount=None, settlementAmount=None, executionPeriodDates=None, earliestExecutionTime=None, latestExecutionTime=None, settlementDateOffset=None, finalSettlementDate=None, forwardRate=None, additionalPayment=None):
        super(FxFlexibleForwardSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, putCurrency, callCurrency, notionalAmount, minimumExecutionAmount, settlementAmount, executionPeriodDates, earliestExecutionTime, latestExecutionTime, settlementDateOffset, finalSettlementDate, forwardRate, additionalPayment, )
supermod.FxFlexibleForward.subclass = FxFlexibleForwardSub
# end class FxFlexibleForwardSub


class FxFlexibleForwardExecutionPeriodSub(supermod.FxFlexibleForwardExecutionPeriod):
    def __init__(self, id=None, startDate=None, expiryDate=None, businessCenters=None):
        super(FxFlexibleForwardExecutionPeriodSub, self).__init__(id, startDate, expiryDate, businessCenters, )
supermod.FxFlexibleForwardExecutionPeriod.subclass = FxFlexibleForwardExecutionPeriodSub
# end class FxFlexibleForwardExecutionPeriodSub


class FxFlexibleForwardRateSub(supermod.FxFlexibleForwardRate):
    def __init__(self, currency1=None, currency2=None, quoteBasis=None, rate=None, spotRate=None):
        super(FxFlexibleForwardRateSub, self).__init__(currency1, currency2, quoteBasis, rate, spotRate, )
supermod.FxFlexibleForwardRate.subclass = FxFlexibleForwardRateSub
# end class FxFlexibleForwardRateSub


class FxForwardVolatilityAgreementSub(supermod.FxForwardVolatilityAgreement):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, quotedCurrencyPair=None, fixingDate=None, fixingTime=None, forwardVolatilityStrikePrice=None, straddle=None, additionalPayment=None):
        super(FxForwardVolatilityAgreementSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, quotedCurrencyPair, fixingDate, fixingTime, forwardVolatilityStrikePrice, straddle, additionalPayment, )
supermod.FxForwardVolatilityAgreement.subclass = FxForwardVolatilityAgreementSub
# end class FxForwardVolatilityAgreementSub


class FxMultipleExerciseSub(supermod.FxMultipleExercise):
    def __init__(self, minimumNotionalAmount=None, maximumNotionalAmount=None):
        super(FxMultipleExerciseSub, self).__init__(minimumNotionalAmount, maximumNotionalAmount, )
supermod.FxMultipleExercise.subclass = FxMultipleExerciseSub
# end class FxMultipleExerciseSub


class FxOptionSub(supermod.FxOption):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, effectiveDate=None, tenorPeriod=None, americanExercise=None, europeanExercise=None, exerciseProcedure=None, putCurrencyAmount=None, callCurrencyAmount=None, soldAs=None, strike=None, spotRate=None, features=None, premium=None, cashSettlement=None):
        super(FxOptionSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, effectiveDate, tenorPeriod, americanExercise, europeanExercise, exerciseProcedure, putCurrencyAmount, callCurrencyAmount, soldAs, strike, spotRate, features, premium, cashSettlement, )
supermod.FxOption.subclass = FxOptionSub
# end class FxOptionSub


class FxOptionFeaturesSub(supermod.FxOptionFeatures):
    def __init__(self, asian=None, barrier=None):
        super(FxOptionFeaturesSub, self).__init__(asian, barrier, )
supermod.FxOptionFeatures.subclass = FxOptionFeaturesSub
# end class FxOptionFeaturesSub


class FxOptionPayoutSub(supermod.FxOptionPayout):
    def __init__(self, id=None, currency=None, amount=None, payoutStyle=None, settlementInformation=None):
        super(FxOptionPayoutSub, self).__init__(id, currency, amount, payoutStyle, settlementInformation, )
supermod.FxOptionPayout.subclass = FxOptionPayoutSub
# end class FxOptionPayoutSub


class FxPerformanceLegSub(supermod.FxPerformanceLeg):
    def __init__(self, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, extensiontype_=None):
        super(FxPerformanceLegSub, self).__init__(payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, extensiontype_, )
supermod.FxPerformanceLeg.subclass = FxPerformanceLegSub
# end class FxPerformanceLegSub


class FxPerformanceSwapSub(supermod.FxPerformanceSwap):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, quotedCurrencyPair=None, vegaNotional=None, notional=None, fixedLeg=None, floatingLeg=None, fixingInformationSource=None, fixingSchedule=None, valuationDate=None, valuationDateOffset=None, settlementDate=None, annualizationFactor=None, meanAdjustment=None, numberOfReturns=None, additionalPayment=None, cashSettlement=None):
        super(FxPerformanceSwapSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, quotedCurrencyPair, vegaNotional, notional, fixedLeg, floatingLeg, fixingInformationSource, fixingSchedule, valuationDate, valuationDateOffset, settlementDate, annualizationFactor, meanAdjustment, numberOfReturns, additionalPayment, cashSettlement, )
supermod.FxPerformanceSwap.subclass = FxPerformanceSwapSub
# end class FxPerformanceSwapSub


class FxSingleLegSub(supermod.FxSingleLeg):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, exchangedCurrency1=None, exchangedCurrency2=None, dealtCurrency=None, tenorName=None, tenorPeriod=None, valueDate=None, currency1ValueDate=None, currency2ValueDate=None, exchangeRate=None, nonDeliverableSettlement=None, disruption=None):
        super(FxSingleLegSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, exchangedCurrency1, exchangedCurrency2, dealtCurrency, tenorName, tenorPeriod, valueDate, currency1ValueDate, currency2ValueDate, exchangeRate, nonDeliverableSettlement, disruption, )
supermod.FxSingleLeg.subclass = FxSingleLegSub
# end class FxSingleLegSub


class FxStraddleSub(supermod.FxStraddle):
    def __init__(self, straddleType=None, tenorPeriod=None, europeanExercise=None, exerciseProcedure=None, notional=None, counterCurrency=None, premium=None, settlementDate=None, cashSettlement=None):
        super(FxStraddleSub, self).__init__(straddleType, tenorPeriod, europeanExercise, exerciseProcedure, notional, counterCurrency, premium, settlementDate, cashSettlement, )
supermod.FxStraddle.subclass = FxStraddleSub
# end class FxStraddleSub


class FxStraddlePremiumSub(supermod.FxStraddlePremium):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentDate=None, paymentCurrency=None, settlementInformation=None):
        super(FxStraddlePremiumSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentDate, paymentCurrency, settlementInformation, )
supermod.FxStraddlePremium.subclass = FxStraddlePremiumSub
# end class FxStraddlePremiumSub


class FxStrikePriceSub(supermod.FxStrikePrice):
    def __init__(self, rate=None, strikeQuoteBasis=None):
        super(FxStrikePriceSub, self).__init__(rate, strikeQuoteBasis, )
supermod.FxStrikePrice.subclass = FxStrikePriceSub
# end class FxStrikePriceSub


class FxSwapSub(supermod.FxSwap):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, nearLeg=None, farLeg=None):
        super(FxSwapSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, nearLeg, farLeg, )
supermod.FxSwap.subclass = FxSwapSub
# end class FxSwapSub


class FxSwapLegSub(supermod.FxSwapLeg):
    def __init__(self, id=None, tradeIdentifierReference=None, exchangedCurrency1=None, exchangedCurrency2=None, dealtCurrency=None, tenorName=None, tenorPeriod=None, valueDate=None, currency1ValueDate=None, currency2ValueDate=None, exchangeRate=None, nonDeliverableSettlement=None, disruption=None):
        super(FxSwapLegSub, self).__init__(id, tradeIdentifierReference, exchangedCurrency1, exchangedCurrency2, dealtCurrency, tenorName, tenorPeriod, valueDate, currency1ValueDate, currency2ValueDate, exchangeRate, nonDeliverableSettlement, disruption, )
supermod.FxSwapLeg.subclass = FxSwapLegSub
# end class FxSwapLegSub


class FxTemplateTermsSub(supermod.FxTemplateTerms):
    def __init__(self, fxTemplateTermsScheme='http://www.fpml.org/coding-scheme/fx-template-terms', valueOf_=None):
        super(FxTemplateTermsSub, self).__init__(fxTemplateTermsScheme, valueOf_, )
supermod.FxTemplateTerms.subclass = FxTemplateTermsSub
# end class FxTemplateTermsSub


class FxTouchSub(supermod.FxTouch):
    def __init__(self, touchCondition=None, direction=None, quotedCurrencyPair=None, triggerRate=None, spotRate=None, informationSource=None, observationStartDate=None, observationStartTime=None, observationEndDate=None, observationEndTime=None, observationPoint=None):
        super(FxTouchSub, self).__init__(touchCondition, direction, quotedCurrencyPair, triggerRate, spotRate, informationSource, observationStartDate, observationStartTime, observationEndDate, observationEndTime, observationPoint, )
supermod.FxTouch.subclass = FxTouchSub
# end class FxTouchSub


class FxTriggerBaseSub(supermod.FxTriggerBase):
    def __init__(self, triggerCondition=None, quotedCurrencyPair=None, triggerRate=None, spotRate=None, extensiontype_=None):
        super(FxTriggerBaseSub, self).__init__(triggerCondition, quotedCurrencyPair, triggerRate, spotRate, extensiontype_, )
supermod.FxTriggerBase.subclass = FxTriggerBaseSub
# end class FxTriggerBaseSub


class NonDeliverableSubstituteSub(supermod.NonDeliverableSubstitute):
    def __init__(self, currency=None):
        super(NonDeliverableSubstituteSub, self).__init__(currency, )
supermod.NonDeliverableSubstitute.subclass = NonDeliverableSubstituteSub
# end class NonDeliverableSubstituteSub


class PostponementSub(supermod.Postponement):
    def __init__(self, maximumNumberOfDays=None):
        super(PostponementSub, self).__init__(maximumNumberOfDays, )
supermod.Postponement.subclass = PostponementSub
# end class PostponementSub


class PremiumQuoteSub(supermod.PremiumQuote):
    def __init__(self, value=None, quoteBasis=None):
        super(PremiumQuoteSub, self).__init__(value, quoteBasis, )
supermod.PremiumQuote.subclass = PremiumQuoteSub
# end class PremiumQuoteSub


class PriceMaterialitySub(supermod.PriceMateriality):
    def __init__(self, primaryRateSource=None, secondaryRateSource=None, percentage=None):
        super(PriceMaterialitySub, self).__init__(primaryRateSource, secondaryRateSource, percentage, )
supermod.PriceMateriality.subclass = PriceMaterialitySub
# end class PriceMaterialitySub


class TermDepositSub(supermod.TermDeposit):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, startDate=None, maturityDate=None, tenorName=None, tenorPeriod=None, principal=None, fixedRate=None, dayCountFraction=None, features=None, interest=None, payment=None):
        super(TermDepositSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, startDate, maturityDate, tenorName, tenorPeriod, principal, fixedRate, dayCountFraction, features, interest, payment, )
supermod.TermDeposit.subclass = TermDepositSub
# end class TermDepositSub


class TermDepositFeaturesSub(supermod.TermDepositFeatures):
    def __init__(self, dualCurrency=None):
        super(TermDepositFeaturesSub, self).__init__(dualCurrency, )
supermod.TermDepositFeatures.subclass = TermDepositFeaturesSub
# end class TermDepositFeaturesSub


class AdditionalDisruptionEventsSub(supermod.AdditionalDisruptionEvents):
    def __init__(self, changeInLaw=None, failureToDeliver=None, insolvencyFiling=None, hedgingDisruption=None, lossOfStockBorrow=None, maximumStockLoanRate=None, increasedCostOfStockBorrow=None, initialStockLoanRate=None, increasedCostOfHedging=None, determiningPartyReference=None, foreignOwnershipEvent=None):
        super(AdditionalDisruptionEventsSub, self).__init__(changeInLaw, failureToDeliver, insolvencyFiling, hedgingDisruption, lossOfStockBorrow, maximumStockLoanRate, increasedCostOfStockBorrow, initialStockLoanRate, increasedCostOfHedging, determiningPartyReference, foreignOwnershipEvent, )
supermod.AdditionalDisruptionEvents.subclass = AdditionalDisruptionEventsSub
# end class AdditionalDisruptionEventsSub


class AdditionalPaymentAmountSub(supermod.AdditionalPaymentAmount):
    def __init__(self, paymentAmount=None, formula=None):
        super(AdditionalPaymentAmountSub, self).__init__(paymentAmount, formula, )
supermod.AdditionalPaymentAmount.subclass = AdditionalPaymentAmountSub
# end class AdditionalPaymentAmountSub


class AdjustableDateOrRelativeDateSequenceSub(supermod.AdjustableDateOrRelativeDateSequence):
    def __init__(self, id=None, adjustableDate=None, relativeDateSequence=None):
        super(AdjustableDateOrRelativeDateSequenceSub, self).__init__(id, adjustableDate, relativeDateSequence, )
supermod.AdjustableDateOrRelativeDateSequence.subclass = AdjustableDateOrRelativeDateSequenceSub
# end class AdjustableDateOrRelativeDateSequenceSub


class BoundedCorrelationSub(supermod.BoundedCorrelation):
    def __init__(self, minimumBoundaryPercent=None, maximumBoundaryPercent=None):
        super(BoundedCorrelationSub, self).__init__(minimumBoundaryPercent, maximumBoundaryPercent, )
supermod.BoundedCorrelation.subclass = BoundedCorrelationSub
# end class BoundedCorrelationSub


class BoundedVarianceSub(supermod.BoundedVariance):
    def __init__(self, realisedVarianceMethod=None, daysInRangeAdjustment=None, upperBarrier=None, lowerBarrier=None):
        super(BoundedVarianceSub, self).__init__(realisedVarianceMethod, daysInRangeAdjustment, upperBarrier, lowerBarrier, )
supermod.BoundedVariance.subclass = BoundedVarianceSub
# end class BoundedVarianceSub


class CalculatedAmountSub(supermod.CalculatedAmount):
    def __init__(self, calculationDates=None, observationStartDate=None, optionsExchangeDividends=None, additionalDividends=None, allDividends=None):
        super(CalculatedAmountSub, self).__init__(calculationDates, observationStartDate, optionsExchangeDividends, additionalDividends, allDividends, )
supermod.CalculatedAmount.subclass = CalculatedAmountSub
# end class CalculatedAmountSub


class CalculationFromObservationSub(supermod.CalculationFromObservation):
    def __init__(self, initialLevel=None, initialLevelSource=None, closingLevel=None, expiringLevel=None, expectedN=None, extensiontype_=None):
        super(CalculationFromObservationSub, self).__init__(initialLevel, initialLevelSource, closingLevel, expiringLevel, expectedN, extensiontype_, )
supermod.CalculationFromObservation.subclass = CalculationFromObservationSub
# end class CalculationFromObservationSub


class CompoundingSub(supermod.Compounding):
    def __init__(self, compoundingMethod=None, compoundingRate=None, compoundingSpread=None, compoundingDates=None):
        super(CompoundingSub, self).__init__(compoundingMethod, compoundingRate, compoundingSpread, compoundingDates, )
supermod.Compounding.subclass = CompoundingSub
# end class CompoundingSub


class CompoundingRateSub(supermod.CompoundingRate):
    def __init__(self, interestLegRate=None, specificRate=None):
        super(CompoundingRateSub, self).__init__(interestLegRate, specificRate, )
supermod.CompoundingRate.subclass = CompoundingRateSub
# end class CompoundingRateSub


class CorrelationSub(supermod.Correlation):
    def __init__(self, initialLevel=None, initialLevelSource=None, closingLevel=None, expiringLevel=None, expectedN=None, notionalAmount=None, correlationStrikePrice=None, boundedCorrelation=None, numberOfDataSeries=None):
        super(CorrelationSub, self).__init__(initialLevel, initialLevelSource, closingLevel, expiringLevel, expectedN, notionalAmount, correlationStrikePrice, boundedCorrelation, numberOfDataSeries, )
supermod.Correlation.subclass = CorrelationSub
# end class CorrelationSub


class DividendAdjustmentSub(supermod.DividendAdjustment):
    def __init__(self, dividendPeriod=None):
        super(DividendAdjustmentSub, self).__init__(dividendPeriod, )
supermod.DividendAdjustment.subclass = DividendAdjustmentSub
# end class DividendAdjustmentSub


class DividendConditionsSub(supermod.DividendConditions):
    def __init__(self, dividendReinvestment=None, dividendEntitlement=None, dividendAmount=None, dividendPaymentDate=None, dividendPeriodEffectiveDate=None, dividendPeriodEndDate=None, dividendPeriod=None, extraOrdinaryDividends=None, excessDividendAmount=None, currency=None, determinationMethod=None, currencyReference=None, dividendFxTriggerDate=None, interestAccrualsMethod=None, numberOfIndexUnits=None, declaredCashDividendPercentage=None, declaredCashEquivalentDividendPercentage=None, nonCashDividendTreatment=None, dividendComposition=None, specialDividends=None):
        super(DividendConditionsSub, self).__init__(dividendReinvestment, dividendEntitlement, dividendAmount, dividendPaymentDate, dividendPeriodEffectiveDate, dividendPeriodEndDate, dividendPeriod, extraOrdinaryDividends, excessDividendAmount, currency, determinationMethod, currencyReference, dividendFxTriggerDate, interestAccrualsMethod, numberOfIndexUnits, declaredCashDividendPercentage, declaredCashEquivalentDividendPercentage, nonCashDividendTreatment, dividendComposition, specialDividends, )
supermod.DividendConditions.subclass = DividendConditionsSub
# end class DividendConditionsSub


class DividendPaymentDateSub(supermod.DividendPaymentDate):
    def __init__(self, dividendDateReference=None, paymentDateOffset=None, adjustableDate=None):
        super(DividendPaymentDateSub, self).__init__(dividendDateReference, paymentDateOffset, adjustableDate, )
supermod.DividendPaymentDate.subclass = DividendPaymentDateSub
# end class DividendPaymentDateSub


class DividendPeriodSub(supermod.DividendPeriod):
    def __init__(self, id=None, unadjustedStartDate=None, unadjustedEndDate=None, dateAdjustments=None, underlyerReference=None, extensiontype_=None):
        super(DividendPeriodSub, self).__init__(id, unadjustedStartDate, unadjustedEndDate, dateAdjustments, underlyerReference, extensiontype_, )
supermod.DividendPeriod.subclass = DividendPeriodSub
# end class DividendPeriodSub


class DividendPeriodDividendSub(supermod.DividendPeriodDividend):
    def __init__(self, id=None, unadjustedStartDate=None, unadjustedEndDate=None, dateAdjustments=None, underlyerReference=None, dividend=None, multiplier=None):
        super(DividendPeriodDividendSub, self).__init__(id, unadjustedStartDate, unadjustedEndDate, dateAdjustments, underlyerReference, dividend, multiplier, )
supermod.DividendPeriodDividend.subclass = DividendPeriodDividendSub
# end class DividendPeriodDividendSub


class EquityCorporateEventsSub(supermod.EquityCorporateEvents):
    def __init__(self, shareForShare=None, shareForOther=None, shareForCombined=None):
        super(EquityCorporateEventsSub, self).__init__(shareForShare, shareForOther, shareForCombined, )
supermod.EquityCorporateEvents.subclass = EquityCorporateEventsSub
# end class EquityCorporateEventsSub


class EquityPremiumSub(supermod.EquityPremium):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, premiumType=None, paymentAmount=None, paymentDate=None, swapPremium=None, pricePerOption=None, percentageOfNotional=None):
        super(EquityPremiumSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, premiumType, paymentAmount, paymentDate, swapPremium, pricePerOption, percentageOfNotional, )
supermod.EquityPremium.subclass = EquityPremiumSub
# end class EquityPremiumSub


class EquityStrikeSub(supermod.EquityStrike):
    def __init__(self, strikePrice=None, strikePercentage=None, strikeDeterminationDate=None, currency=None, extensiontype_=None):
        super(EquityStrikeSub, self).__init__(strikePrice, strikePercentage, strikeDeterminationDate, currency, extensiontype_, )
supermod.EquityStrike.subclass = EquityStrikeSub
# end class EquityStrikeSub


class EquityValuationSub(supermod.EquityValuation):
    def __init__(self, id=None, valuationDate=None, valuationDates=None, valuationTimeType=None, valuationTime=None, futuresPriceValuation=None, optionsPriceValuation=None, numberOfValuationDates=None, dividendValuationDates=None, fPVFinalPriceElectionFallback=None):
        super(EquityValuationSub, self).__init__(id, valuationDate, valuationDates, valuationTimeType, valuationTime, futuresPriceValuation, optionsPriceValuation, numberOfValuationDates, dividendValuationDates, fPVFinalPriceElectionFallback, )
supermod.EquityValuation.subclass = EquityValuationSub
# end class EquityValuationSub


class ExtraordinaryEventsSub(supermod.ExtraordinaryEvents):
    def __init__(self, mergerEvents=None, tenderOffer=None, tenderOfferEvents=None, compositionOfCombinedConsideration=None, indexAdjustmentEvents=None, additionalDisruptionEvents=None, failureToDeliver=None, representations=None, nationalisationOrInsolvency=None, delisting=None, relatedExchangeId=None, optionsExchangeId=None, specifiedExchangeId=None):
        super(ExtraordinaryEventsSub, self).__init__(mergerEvents, tenderOffer, tenderOfferEvents, compositionOfCombinedConsideration, indexAdjustmentEvents, additionalDisruptionEvents, failureToDeliver, representations, nationalisationOrInsolvency, delisting, relatedExchangeId, optionsExchangeId, specifiedExchangeId, )
supermod.ExtraordinaryEvents.subclass = ExtraordinaryEventsSub
# end class ExtraordinaryEventsSub


class FloatingRateCalculationReferenceSub(supermod.FloatingRateCalculationReference):
    def __init__(self, href=None):
        super(FloatingRateCalculationReferenceSub, self).__init__(href, )
supermod.FloatingRateCalculationReference.subclass = FloatingRateCalculationReferenceSub
# end class FloatingRateCalculationReferenceSub


class IndexAdjustmentEventsSub(supermod.IndexAdjustmentEvents):
    def __init__(self, indexModification=None, indexCancellation=None, indexDisruption=None):
        super(IndexAdjustmentEventsSub, self).__init__(indexModification, indexCancellation, indexDisruption, )
supermod.IndexAdjustmentEvents.subclass = IndexAdjustmentEventsSub
# end class IndexAdjustmentEventsSub


class InterestCalculationSub(supermod.InterestCalculation):
    def __init__(self, floatingRateCalculation=None, fixedRate=None, id=None, dayCountFraction=None, compounding=None, interpolationMethod=None, interpolationPeriod=None):
        super(InterestCalculationSub, self).__init__(floatingRateCalculation, fixedRate, id, dayCountFraction, compounding, interpolationMethod, interpolationPeriod, )
supermod.InterestCalculation.subclass = InterestCalculationSub
# end class InterestCalculationSub


class InterestLegCalculationPeriodDatesSub(supermod.InterestLegCalculationPeriodDates):
    def __init__(self, id=None, effectiveDate=None, terminationDate=None, interestLegResetDates=None, interestLegPaymentDates=None):
        super(InterestLegCalculationPeriodDatesSub, self).__init__(id, effectiveDate, terminationDate, interestLegResetDates, interestLegPaymentDates, )
supermod.InterestLegCalculationPeriodDates.subclass = InterestLegCalculationPeriodDatesSub
# end class InterestLegCalculationPeriodDatesSub


class InterestLegCalculationPeriodDatesReferenceSub(supermod.InterestLegCalculationPeriodDatesReference):
    def __init__(self, href=None):
        super(InterestLegCalculationPeriodDatesReferenceSub, self).__init__(href, )
supermod.InterestLegCalculationPeriodDatesReference.subclass = InterestLegCalculationPeriodDatesReferenceSub
# end class InterestLegCalculationPeriodDatesReferenceSub


class InterestLegResetDatesSub(supermod.InterestLegResetDates):
    def __init__(self, calculationPeriodDatesReference=None, resetRelativeTo=None, resetFrequency=None, initialFixingDate=None, fixingDates=None):
        super(InterestLegResetDatesSub, self).__init__(calculationPeriodDatesReference, resetRelativeTo, resetFrequency, initialFixingDate, fixingDates, )
supermod.InterestLegResetDates.subclass = InterestLegResetDatesSub
# end class InterestLegResetDatesSub


class LegAmountSub(supermod.LegAmount):
    def __init__(self, currency=None, determinationMethod=None, currencyReference=None, referenceAmount=None, formula=None, encodedDescription=None, calculationDates=None, extensiontype_=None):
        super(LegAmountSub, self).__init__(currency, determinationMethod, currencyReference, referenceAmount, formula, encodedDescription, calculationDates, extensiontype_, )
supermod.LegAmount.subclass = LegAmountSub
# end class LegAmountSub


class MakeWholeProvisionsSub(supermod.MakeWholeProvisions):
    def __init__(self, makeWholeDate=None, recallSpread=None):
        super(MakeWholeProvisionsSub, self).__init__(makeWholeDate, recallSpread, )
supermod.MakeWholeProvisions.subclass = MakeWholeProvisionsSub
# end class MakeWholeProvisionsSub


class NettedSwapBaseSub(supermod.NettedSwapBase):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, additionalPayment=None, extraordinaryEvents=None):
        super(NettedSwapBaseSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, additionalPayment, extraordinaryEvents, )
supermod.NettedSwapBase.subclass = NettedSwapBaseSub
# end class NettedSwapBaseSub


class OptionFeaturesSub(supermod.OptionFeatures):
    def __init__(self, asian=None, barrier=None, knock=None, passThrough=None, dividendAdjustment=None):
        super(OptionFeaturesSub, self).__init__(asian, barrier, knock, passThrough, dividendAdjustment, )
supermod.OptionFeatures.subclass = OptionFeaturesSub
# end class OptionFeaturesSub


class PrincipalExchangeAmountSub(supermod.PrincipalExchangeAmount):
    def __init__(self, amountRelativeTo=None, determinationMethod=None, principalAmount=None):
        super(PrincipalExchangeAmountSub, self).__init__(amountRelativeTo, determinationMethod, principalAmount, )
supermod.PrincipalExchangeAmount.subclass = PrincipalExchangeAmountSub
# end class PrincipalExchangeAmountSub


class PrincipalExchangeDescriptionsSub(supermod.PrincipalExchangeDescriptions):
    def __init__(self, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, principalExchangeAmount=None, principalExchangeDate=None):
        super(PrincipalExchangeDescriptionsSub, self).__init__(payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, principalExchangeAmount, principalExchangeDate, )
supermod.PrincipalExchangeDescriptions.subclass = PrincipalExchangeDescriptionsSub
# end class PrincipalExchangeDescriptionsSub


class PrincipalExchangeFeaturesSub(supermod.PrincipalExchangeFeatures):
    def __init__(self, principalExchanges=None, principalExchangeDescriptions=None):
        super(PrincipalExchangeFeaturesSub, self).__init__(principalExchanges, principalExchangeDescriptions, )
supermod.PrincipalExchangeFeatures.subclass = PrincipalExchangeFeaturesSub
# end class PrincipalExchangeFeaturesSub


class RepresentationsSub(supermod.Representations):
    def __init__(self, nonReliance=None, agreementsRegardingHedging=None, indexDisclaimer=None, additionalAcknowledgements=None):
        super(RepresentationsSub, self).__init__(nonReliance, agreementsRegardingHedging, indexDisclaimer, additionalAcknowledgements, )
supermod.Representations.subclass = RepresentationsSub
# end class RepresentationsSub


class ReturnSub(supermod.Return):
    def __init__(self, returnType=None, dividendConditions=None):
        super(ReturnSub, self).__init__(returnType, dividendConditions, )
supermod.Return.subclass = ReturnSub
# end class ReturnSub


class ReturnLegValuationSub(supermod.ReturnLegValuation):
    def __init__(self, initialPrice=None, notionalReset=None, valuationPriceInterim=None, valuationPriceFinal=None, paymentDates=None, exchangeTradedContractNearest=None):
        super(ReturnLegValuationSub, self).__init__(initialPrice, notionalReset, valuationPriceInterim, valuationPriceFinal, paymentDates, exchangeTradedContractNearest, )
supermod.ReturnLegValuation.subclass = ReturnLegValuationSub
# end class ReturnLegValuationSub


class ReturnLegValuationPriceSub(supermod.ReturnLegValuationPrice):
    def __init__(self, commission=None, determinationMethod=None, grossPrice=None, netPrice=None, accruedInterestPrice=None, fxConversion=None, amountRelativeTo=None, cleanNetPrice=None, quotationCharacteristics=None, valuationRules=None):
        super(ReturnLegValuationPriceSub, self).__init__(commission, determinationMethod, grossPrice, netPrice, accruedInterestPrice, fxConversion, amountRelativeTo, cleanNetPrice, quotationCharacteristics, valuationRules, )
supermod.ReturnLegValuationPrice.subclass = ReturnLegValuationPriceSub
# end class ReturnLegValuationPriceSub


class ReturnSwapAdditionalPaymentSub(supermod.ReturnSwapAdditionalPayment):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, additionalPaymentAmount=None, additionalPaymentDate=None, paymentType=None):
        super(ReturnSwapAdditionalPaymentSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, additionalPaymentAmount, additionalPaymentDate, paymentType, )
supermod.ReturnSwapAdditionalPayment.subclass = ReturnSwapAdditionalPaymentSub
# end class ReturnSwapAdditionalPaymentSub


class ReturnSwapAmountSub(supermod.ReturnSwapAmount):
    def __init__(self, currency=None, determinationMethod=None, currencyReference=None, referenceAmount=None, formula=None, encodedDescription=None, calculationDates=None, cashSettlement=None, optionsExchangeDividends=None, additionalDividends=None, allDividends=None):
        super(ReturnSwapAmountSub, self).__init__(currency, determinationMethod, currencyReference, referenceAmount, formula, encodedDescription, calculationDates, cashSettlement, optionsExchangeDividends, additionalDividends, allDividends, )
supermod.ReturnSwapAmount.subclass = ReturnSwapAmountSub
# end class ReturnSwapAmountSub


class ReturnSwapBaseSub(supermod.ReturnSwapBase):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, returnSwapLeg=None, principalExchangeFeatures=None, additionalPayment=None, extensiontype_=None):
        super(ReturnSwapBaseSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, returnSwapLeg, principalExchangeFeatures, additionalPayment, extensiontype_, )
supermod.ReturnSwapBase.subclass = ReturnSwapBaseSub
# end class ReturnSwapBaseSub


class ReturnSwapEarlyTerminationSub(supermod.ReturnSwapEarlyTermination):
    def __init__(self, partyReference=None, startingDate=None):
        super(ReturnSwapEarlyTerminationSub, self).__init__(partyReference, startingDate, )
supermod.ReturnSwapEarlyTermination.subclass = ReturnSwapEarlyTerminationSub
# end class ReturnSwapEarlyTerminationSub


class ReturnSwapNotionalSub(supermod.ReturnSwapNotional):
    def __init__(self, id=None, relativeNotionalAmount=None, relativeDeterminationMethod=None, determinationMethod=None, notionalAmount=None):
        super(ReturnSwapNotionalSub, self).__init__(id, relativeNotionalAmount, relativeDeterminationMethod, determinationMethod, notionalAmount, )
supermod.ReturnSwapNotional.subclass = ReturnSwapNotionalSub
# end class ReturnSwapNotionalSub


class ReturnSwapPaymentDatesSub(supermod.ReturnSwapPaymentDates):
    def __init__(self, id=None, paymentDatesInterim=None, paymentDateFinal=None):
        super(ReturnSwapPaymentDatesSub, self).__init__(id, paymentDatesInterim, paymentDateFinal, )
supermod.ReturnSwapPaymentDates.subclass = ReturnSwapPaymentDatesSub
# end class ReturnSwapPaymentDatesSub


class StartingDateSub(supermod.StartingDate):
    def __init__(self, dateRelativeTo=None, adjustableDate=None):
        super(StartingDateSub, self).__init__(dateRelativeTo, adjustableDate, )
supermod.StartingDate.subclass = StartingDateSub
# end class StartingDateSub


class StubCalculationPeriodSub(supermod.StubCalculationPeriod):
    def __init__(self, initialStub=None, finalStub=None):
        super(StubCalculationPeriodSub, self).__init__(initialStub, finalStub, )
supermod.StubCalculationPeriod.subclass = StubCalculationPeriodSub
# end class StubCalculationPeriodSub


class VarianceSub(supermod.Variance):
    def __init__(self, initialLevel=None, initialLevelSource=None, closingLevel=None, expiringLevel=None, expectedN=None, varianceAmount=None, volatilityStrikePrice=None, varianceStrikePrice=None, varianceCap=None, unadjustedVarianceCap=None, boundedVariance=None, exchangeTradedContractNearest=None, vegaNotionalAmount=None):
        super(VarianceSub, self).__init__(initialLevel, initialLevelSource, closingLevel, expiringLevel, expectedN, varianceAmount, volatilityStrikePrice, varianceStrikePrice, varianceCap, unadjustedVarianceCap, boundedVariance, exchangeTradedContractNearest, vegaNotionalAmount, )
supermod.Variance.subclass = VarianceSub
# end class VarianceSub


class ReturnSwapSub(supermod.ReturnSwap):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, returnSwapLeg=None, principalExchangeFeatures=None, additionalPayment=None, earlyTermination=None, extraordinaryEvents=None):
        super(ReturnSwapSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, returnSwapLeg, principalExchangeFeatures, additionalPayment, earlyTermination, extraordinaryEvents, )
supermod.ReturnSwap.subclass = ReturnSwapSub
# end class ReturnSwapSub


class FxTriggerSub(supermod.FxTrigger):
    def __init__(self, triggerCondition=None, quotedCurrencyPair=None, triggerRate=None, spotRate=None, informationSource=None):
        super(FxTriggerSub, self).__init__(triggerCondition, quotedCurrencyPair, triggerRate, spotRate, informationSource, )
supermod.FxTrigger.subclass = FxTriggerSub
# end class FxTriggerSub


class FxPerformanceFloatingLegSub(supermod.FxPerformanceFloatingLeg):
    def __init__(self, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None):
        super(FxPerformanceFloatingLegSub, self).__init__(payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, )
supermod.FxPerformanceFloatingLeg.subclass = FxPerformanceFloatingLegSub
# end class FxPerformanceFloatingLegSub


class FxPerformanceFixedLegSub(supermod.FxPerformanceFixedLeg):
    def __init__(self, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, fixedRate=None):
        super(FxPerformanceFixedLegSub, self).__init__(payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, fixedRate, )
supermod.FxPerformanceFixedLeg.subclass = FxPerformanceFixedLegSub
# end class FxPerformanceFixedLegSub


class FxAmericanExerciseSub(supermod.FxAmericanExercise):
    def __init__(self, id=None, commencementDate=None, expiryDate=None, expiryTime=None, cutName=None, latestValueDate=None, multipleExercise=None):
        super(FxAmericanExerciseSub, self).__init__(id, commencementDate, expiryDate, expiryTime, cutName, latestValueDate, multipleExercise, )
supermod.FxAmericanExercise.subclass = FxAmericanExerciseSub
# end class FxAmericanExerciseSub


class OilPhysicalLegSub(supermod.OilPhysicalLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, deliveryPeriods=None, oil=None, deliveryConditions=None, deliveryQuantity=None):
        super(OilPhysicalLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, deliveryPeriods, oil, deliveryConditions, deliveryQuantity, )
supermod.OilPhysicalLeg.subclass = OilPhysicalLegSub
# end class OilPhysicalLegSub


class MetalPhysicalLegSub(supermod.MetalPhysicalLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, metal=None, deliveryPeriods=None, deliveryConditions=None, physicalQuantity=None, physicalQuantitySchedule=None, totalPhysicalQuantity=None, conversionFactor=None):
        super(MetalPhysicalLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, metal, deliveryPeriods, deliveryConditions, physicalQuantity, physicalQuantitySchedule, totalPhysicalQuantity, conversionFactor, )
supermod.MetalPhysicalLeg.subclass = MetalPhysicalLegSub
# end class MetalPhysicalLegSub


class GasPhysicalLegSub(supermod.GasPhysicalLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, deliveryPeriods=None, gas=None, deliveryConditions=None, deliveryQuantity=None):
        super(GasPhysicalLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, deliveryPeriods, gas, deliveryConditions, deliveryQuantity, )
supermod.GasPhysicalLeg.subclass = GasPhysicalLegSub
# end class GasPhysicalLegSub


class EnvironmentalPhysicalLegSub(supermod.EnvironmentalPhysicalLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, numberOfAllowances=None, environmental=None, abandonmentOfScheme=None, deliveryDate=None, paymentDate=None, businessCentersReference=None, businessCenters=None, failureToDeliverApplicable=None, eEPParameters=None):
        super(EnvironmentalPhysicalLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, numberOfAllowances, environmental, abandonmentOfScheme, deliveryDate, paymentDate, businessCentersReference, businessCenters, failureToDeliverApplicable, eEPParameters, )
supermod.EnvironmentalPhysicalLeg.subclass = EnvironmentalPhysicalLegSub
# end class EnvironmentalPhysicalLegSub


class ElectricityPhysicalLegSub(supermod.ElectricityPhysicalLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, deliveryPeriods=None, settlementPeriods=None, settlementPeriodsSchedule=None, loadType=None, electricity=None, deliveryConditions=None, deliveryQuantity=None):
        super(ElectricityPhysicalLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, deliveryPeriods, settlementPeriods, settlementPeriodsSchedule, loadType, electricity, deliveryConditions, deliveryQuantity, )
supermod.ElectricityPhysicalLeg.subclass = ElectricityPhysicalLegSub
# end class ElectricityPhysicalLegSub


class CommodityPhysicalQuantitySub(supermod.CommodityPhysicalQuantity):
    def __init__(self, id=None, physicalQuantity=None, physicalQuantitySchedule=None, totalPhysicalQuantity=None):
        super(CommodityPhysicalQuantitySub, self).__init__(id, physicalQuantity, physicalQuantitySchedule, totalPhysicalQuantity, )
supermod.CommodityPhysicalQuantity.subclass = CommodityPhysicalQuantitySub
# end class CommodityPhysicalQuantitySub


class CommodityPerformanceSwapSub(supermod.CommodityPerformanceSwap):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, effectiveDate=None, terminationDate=None, settlementCurrency=None, commodityPerformanceSwapLeg=None, commonPricing=None, marketDisruption=None, settlementDisruption=None, rounding=None, earlyTermination=None):
        super(CommodityPerformanceSwapSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, effectiveDate, terminationDate, settlementCurrency, commodityPerformanceSwapLeg, commonPricing, marketDisruption, settlementDisruption, rounding, earlyTermination, )
supermod.CommodityPerformanceSwap.subclass = CommodityPerformanceSwapSub
# end class CommodityPerformanceSwapSub


class CommodityInterestLegSub(supermod.CommodityInterestLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, calculationDates=None, calculationPeriods=None, calculationPeriodsSchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None, notionalAmount=None, notionalAmountReference=None, commodityFixedInterestCalculation=None):
        super(CommodityInterestLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, calculationDates, calculationPeriods, calculationPeriodsSchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, relativePaymentDates, paymentDates, masterAgreementPaymentDates, notionalAmount, notionalAmountReference, commodityFixedInterestCalculation, )
supermod.CommodityInterestLeg.subclass = CommodityInterestLegSub
# end class CommodityInterestLegSub


class CommodityDigitalOptionSub(supermod.CommodityDigitalOption):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, optionType=None, commodity=None, effectiveDate=None, terminationDate=None, calculationPeriodsSchedule=None, calculationPeriods=None, pricingDates=None, averagingMethod=None, digital=None, notionalAmount=None, notionalQuantity=None, totalNotionalQuantity=None, exercise=None, premium=None, commonPricing=None, marketDisruption=None, settlementDisruption=None, rounding=None):
        super(CommodityDigitalOptionSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, optionType, commodity, effectiveDate, terminationDate, calculationPeriodsSchedule, calculationPeriods, pricingDates, averagingMethod, digital, notionalAmount, notionalQuantity, totalNotionalQuantity, exercise, premium, commonPricing, marketDisruption, settlementDisruption, rounding, )
supermod.CommodityDigitalOption.subclass = CommodityDigitalOptionSub
# end class CommodityDigitalOptionSub


class CommodityBasketOptionSub(supermod.CommodityBasketOption):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, optionType=None, effectiveDate=None, terminationDate=None, calculationPeriodsSchedule=None, calculationPeriods=None, notionalQuantityBasket=None, notionalAmountBasket=None, strikePriceUnderlyingReference=None, strikePriceBasketReference=None, strikePricePerUnit=None, strikePricePerUnitSchedule=None, floatingStrikePricePerUnit=None, floatingStrikePricePerUnitSchedule=None, exercise=None, premium=None, commonPricing=None, marketDisruption=None, settlementDisruption=None, rounding=None):
        super(CommodityBasketOptionSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, optionType, effectiveDate, terminationDate, calculationPeriodsSchedule, calculationPeriods, notionalQuantityBasket, notionalAmountBasket, strikePriceUnderlyingReference, strikePriceBasketReference, strikePricePerUnit, strikePricePerUnitSchedule, floatingStrikePricePerUnit, floatingStrikePricePerUnitSchedule, exercise, premium, commonPricing, marketDisruption, settlementDisruption, rounding, )
supermod.CommodityBasketOption.subclass = CommodityBasketOptionSub
# end class CommodityBasketOptionSub


class CoalPhysicalLegSub(supermod.CoalPhysicalLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, deliveryPeriods=None, coal=None, deliveryConditions=None, deliveryQuantity=None):
        super(CoalPhysicalLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, deliveryPeriods, coal, deliveryConditions, deliveryQuantity, )
supermod.CoalPhysicalLeg.subclass = CoalPhysicalLegSub
# end class CoalPhysicalLegSub


class BullionPhysicalLegSub(supermod.BullionPhysicalLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, bullionType=None, deliveryLocation=None, physicalQuantity=None, physicalQuantitySchedule=None, totalPhysicalQuantity=None, settlementDate=None):
        super(BullionPhysicalLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, bullionType, deliveryLocation, physicalQuantity, physicalQuantitySchedule, totalPhysicalQuantity, settlementDate, )
supermod.BullionPhysicalLeg.subclass = BullionPhysicalLegSub
# end class BullionPhysicalLegSub


class AveragePriceLegSub(supermod.AveragePriceLeg):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, calculationDates=None, calculationPeriods=None, calculationPeriodsSchedule=None, calculationPeriodsReference=None, calculationPeriodsScheduleReference=None, calculationPeriodsDatesReference=None, commodity=None, quantityReference=None, pricingStartDate=None, calculation=None, relativePaymentDates=None, paymentDates=None, masterAgreementPaymentDates=None):
        super(AveragePriceLegSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, calculationDates, calculationPeriods, calculationPeriodsSchedule, calculationPeriodsReference, calculationPeriodsScheduleReference, calculationPeriodsDatesReference, commodity, quantityReference, pricingStartDate, calculation, relativePaymentDates, paymentDates, masterAgreementPaymentDates, )
supermod.AveragePriceLeg.subclass = AveragePriceLegSub
# end class AveragePriceLegSub


class SimpleIRSwapSub(supermod.SimpleIRSwap):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, term=None, paymentFrequency=None, dayCountFraction=None):
        super(SimpleIRSwapSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, term, paymentFrequency, dayCountFraction, )
supermod.SimpleIRSwap.subclass = SimpleIRSwapSub
# end class SimpleIRSwapSub


class SimpleFraSub(supermod.SimpleFra):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, startTerm=None, endTerm=None, dayCountFraction=None):
        super(SimpleFraSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, startTerm, endTerm, dayCountFraction, )
supermod.SimpleFra.subclass = SimpleFraSub
# end class SimpleFraSub


class SimpleCreditDefaultSwapSub(supermod.SimpleCreditDefaultSwap):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, referenceEntity=None, creditEntityReference=None, term=None, paymentFrequency=None):
        super(SimpleCreditDefaultSwapSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, referenceEntity, creditEntityReference, term, paymentFrequency, )
supermod.SimpleCreditDefaultSwap.subclass = SimpleCreditDefaultSwapSub
# end class SimpleCreditDefaultSwapSub


class RateIndexSub(supermod.RateIndex):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, floatingRateIndex=None, term=None, paymentFrequency=None, dayCountFraction=None):
        super(RateIndexSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, floatingRateIndex, term, paymentFrequency, dayCountFraction, )
supermod.RateIndex.subclass = RateIndexSub
# end class RateIndexSub


class MutualFundSub(supermod.MutualFund):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, openEndedFund=None, fundManager=None):
        super(MutualFundSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, openEndedFund, fundManager, )
supermod.MutualFund.subclass = MutualFundSub
# end class MutualFundSub


class MortgageSub(supermod.Mortgage):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, insurer=None, insurerReference=None, issuerName=None, issuerPartyReference=None, seniority=None, couponType=None, couponRate=None, maturity=None, paymentFrequency=None, dayCountFraction=None, originalPrincipalAmount=None, pool=None, sector=None, tranche=None):
        super(MortgageSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, insurer, insurerReference, issuerName, issuerPartyReference, seniority, couponType, couponRate, maturity, paymentFrequency, dayCountFraction, originalPrincipalAmount, pool, sector, tranche, )
supermod.Mortgage.subclass = MortgageSub
# end class MortgageSub


class LoanSub(supermod.Loan):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, borrower=None, borrowerReference=None, lien=None, facilityType=None, maturity=None, creditAgreementDate=None, tranche=None):
        super(LoanSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, borrower, borrowerReference, lien, facilityType, maturity, creditAgreementDate, tranche, )
supermod.Loan.subclass = LoanSub
# end class LoanSub


class FxRateAssetSub(supermod.FxRateAsset):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, quotedCurrencyPair=None, rateSource=None):
        super(FxRateAssetSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, quotedCurrencyPair, rateSource, )
supermod.FxRateAsset.subclass = FxRateAssetSub
# end class FxRateAssetSub


class ExchangeTradedSub(supermod.ExchangeTraded):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, relatedExchangeId=None, optionsExchangeId=None, specifiedExchangeId=None, extensiontype_=None):
        super(ExchangeTradedSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, relatedExchangeId, optionsExchangeId, specifiedExchangeId, extensiontype_, )
supermod.ExchangeTraded.subclass = ExchangeTradedSub
# end class ExchangeTradedSub


class EquityAssetSub(supermod.EquityAsset):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, relatedExchangeId=None, optionsExchangeId=None, specifiedExchangeId=None):
        super(EquityAssetSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, relatedExchangeId, optionsExchangeId, specifiedExchangeId, )
supermod.EquityAsset.subclass = EquityAssetSub
# end class EquityAssetSub


class DepositSub(supermod.Deposit):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, term=None, paymentFrequency=None, dayCountFraction=None):
        super(DepositSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, term, paymentFrequency, dayCountFraction, )
supermod.Deposit.subclass = DepositSub
# end class DepositSub


class CommoditySub(supermod.Commodity):
    def __init__(self, id=None, instrumentId=None, description=None, commodityBase=None, commodityDetails=None, unit=None, currency=None, exchangeId=None, publication=None, specifiedPrice=None, deliveryDates=None, deliveryNearby=None, deliveryDate=None, deliveryDateYearMonth=None, deliveryDateRollConvention=None, deliveryDateExpirationConvention=None, multiplier=None):
        super(CommoditySub, self).__init__(id, instrumentId, description, commodityBase, commodityDetails, unit, currency, exchangeId, publication, specifiedPrice, deliveryDates, deliveryNearby, deliveryDate, deliveryDateYearMonth, deliveryDateRollConvention, deliveryDateExpirationConvention, multiplier, )
supermod.Commodity.subclass = CommoditySub
# end class CommoditySub


class BondSub(supermod.Bond):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, issuerName=None, issuerPartyReference=None, seniority=None, couponType=None, couponRate=None, maturity=None, parValue=None, faceAmount=None, paymentFrequency=None, dayCountFraction=None, extensiontype_=None):
        super(BondSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, issuerName, issuerPartyReference, seniority, couponType, couponRate, maturity, parValue, faceAmount, paymentFrequency, dayCountFraction, extensiontype_, )
supermod.Bond.subclass = BondSub
# end class BondSub


class StubSub(supermod.Stub):
    def __init__(self, floatingRate=None, stubRate=None, stubAmount=None, stubStartDate=None, stubEndDate=None):
        super(StubSub, self).__init__(floatingRate, stubRate, stubAmount, stubStartDate, stubEndDate, )
supermod.Stub.subclass = StubSub
# end class StubSub


class StepSub(supermod.Step):
    def __init__(self, id=None, stepDate=None, stepValue=None):
        super(StepSub, self).__init__(id, stepDate, stepValue, )
supermod.Step.subclass = StepSub
# end class StepSub


class ProductReferenceSub(supermod.ProductReference):
    def __init__(self, href=None):
        super(ProductReferenceSub, self).__init__(href, )
supermod.ProductReference.subclass = ProductReferenceSub
# end class ProductReferenceSub


class PricingStructureReferenceSub(supermod.PricingStructureReference):
    def __init__(self, href=None):
        super(PricingStructureReferenceSub, self).__init__(href, )
supermod.PricingStructureReference.subclass = PricingStructureReferenceSub
# end class PricingStructureReferenceSub


class PaymentReferenceSub(supermod.PaymentReference):
    def __init__(self, href=None):
        super(PaymentReferenceSub, self).__init__(href, )
supermod.PaymentReference.subclass = PaymentReferenceSub
# end class PaymentReferenceSub


class PaymentSub(supermod.Payment):
    def __init__(self, id=None, href=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentAmount=None, paymentDate=None, paymentType=None, settlementInformation=None, discountFactor=None, presentValueAmount=None):
        super(PaymentSub, self).__init__(id, href, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentAmount, paymentDate, paymentType, settlementInformation, discountFactor, presentValueAmount, )
supermod.Payment.subclass = PaymentSub
# end class PaymentSub


class PartyTradeIdentifierReferenceSub(supermod.PartyTradeIdentifierReference):
    def __init__(self, href=None):
        super(PartyTradeIdentifierReferenceSub, self).__init__(href, )
supermod.PartyTradeIdentifierReference.subclass = PartyTradeIdentifierReferenceSub
# end class PartyTradeIdentifierReferenceSub


class PersonReferenceSub(supermod.PersonReference):
    def __init__(self, href=None):
        super(PersonReferenceSub, self).__init__(href, )
supermod.PersonReference.subclass = PersonReferenceSub
# end class PersonReferenceSub


class PartyReferenceSub(supermod.PartyReference):
    def __init__(self, href=None):
        super(PartyReferenceSub, self).__init__(href, )
supermod.PartyReference.subclass = PartyReferenceSub
# end class PartyReferenceSub


class OffsetSub(supermod.Offset):
    def __init__(self, id=None, periodMultiplier=None, period=None, dayType=None, extensiontype_=None):
        super(OffsetSub, self).__init__(id, periodMultiplier, period, dayType, extensiontype_, )
supermod.Offset.subclass = OffsetSub
# end class OffsetSub


class ObservationFrequencySub(supermod.ObservationFrequency):
    def __init__(self, id=None, periodMultiplier=None, period=None, periodConvention=None):
        super(ObservationFrequencySub, self).__init__(id, periodMultiplier, period, periodConvention, )
supermod.ObservationFrequency.subclass = ObservationFrequencySub
# end class ObservationFrequencySub


class NumberOfUnitsReferenceSub(supermod.NumberOfUnitsReference):
    def __init__(self, href=None):
        super(NumberOfUnitsReferenceSub, self).__init__(href, )
supermod.NumberOfUnitsReference.subclass = NumberOfUnitsReferenceSub
# end class NumberOfUnitsReferenceSub


class NumberOfOptionsReferenceSub(supermod.NumberOfOptionsReference):
    def __init__(self, href=None):
        super(NumberOfOptionsReferenceSub, self).__init__(href, )
supermod.NumberOfOptionsReference.subclass = NumberOfOptionsReferenceSub
# end class NumberOfOptionsReferenceSub


class NotionalReferenceSub(supermod.NotionalReference):
    def __init__(self, href=None):
        super(NotionalReferenceSub, self).__init__(href, )
supermod.NotionalReference.subclass = NotionalReferenceSub
# end class NotionalReferenceSub


class NotionalAmountReferenceSub(supermod.NotionalAmountReference):
    def __init__(self, href=None):
        super(NotionalAmountReferenceSub, self).__init__(href, )
supermod.NotionalAmountReference.subclass = NotionalAmountReferenceSub
# end class NotionalAmountReferenceSub


class NonNegativeStepSub(supermod.NonNegativeStep):
    def __init__(self, id=None, stepDate=None, stepValue=None):
        super(NonNegativeStepSub, self).__init__(id, stepDate, stepValue, )
supermod.NonNegativeStep.subclass = NonNegativeStepSub
# end class NonNegativeStepSub


class NonNegativePaymentSub(supermod.NonNegativePayment):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentDate=None, paymentAmount=None, extensiontype_=None):
        super(NonNegativePaymentSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentDate, paymentAmount, extensiontype_, )
supermod.NonNegativePayment.subclass = NonNegativePaymentSub
# end class NonNegativePaymentSub


class NonNegativeAmountScheduleSub(supermod.NonNegativeAmountSchedule):
    def __init__(self, id=None, initialValue=None, step=None, currency=None):
        super(NonNegativeAmountScheduleSub, self).__init__(id, initialValue, step, currency, )
supermod.NonNegativeAmountSchedule.subclass = NonNegativeAmountScheduleSub
# end class NonNegativeAmountScheduleSub


class MoneySub(supermod.Money):
    def __init__(self, id=None, currency=None, amount=None, extensiontype_=None):
        super(MoneySub, self).__init__(id, currency, amount, extensiontype_, )
supermod.Money.subclass = MoneySub
# end class MoneySub


class LegalEntityReferenceSub(supermod.LegalEntityReference):
    def __init__(self, href=None):
        super(LegalEntityReferenceSub, self).__init__(href, )
supermod.LegalEntityReference.subclass = LegalEntityReferenceSub
# end class LegalEntityReferenceSub


class InterestAccrualsCompoundingMethodSub(supermod.InterestAccrualsCompoundingMethod):
    def __init__(self, floatingRateCalculation=None, fixedRate=None, compoundingMethod=None):
        super(InterestAccrualsCompoundingMethodSub, self).__init__(floatingRateCalculation, fixedRate, compoundingMethod, )
supermod.InterestAccrualsCompoundingMethod.subclass = InterestAccrualsCompoundingMethodSub
# end class InterestAccrualsCompoundingMethodSub


class IdentifiedCurrencyReferenceSub(supermod.IdentifiedCurrencyReference):
    def __init__(self, href=None):
        super(IdentifiedCurrencyReferenceSub, self).__init__(href, )
supermod.IdentifiedCurrencyReference.subclass = IdentifiedCurrencyReferenceSub
# end class IdentifiedCurrencyReferenceSub


class FxInformationSourceSub(supermod.FxInformationSource):
    def __init__(self, rateSource=None, rateSourcePage=None, rateSourcePageHeading=None, fixingTime=None):
        super(FxInformationSourceSub, self).__init__(rateSource, rateSourcePage, rateSourcePageHeading, fixingTime, )
supermod.FxInformationSource.subclass = FxInformationSourceSub
# end class FxInformationSourceSub


class FutureValueAmountSub(supermod.FutureValueAmount):
    def __init__(self, id=None, currency=None, amount=None, calculationPeriodNumberOfDays=None, valueDate=None):
        super(FutureValueAmountSub, self).__init__(id, currency, amount, calculationPeriodNumberOfDays, valueDate, )
supermod.FutureValueAmount.subclass = FutureValueAmountSub
# end class FutureValueAmountSub


class FloatingRateSub(supermod.FloatingRate):
    def __init__(self, id=None, floatingRateIndex=None, indexTenor=None, floatingRateMultiplierSchedule=None, spreadSchedule=None, rateTreatment=None, capRateSchedule=None, floorRateSchedule=None, capFloorStraddle=None, extensiontype_=None):
        super(FloatingRateSub, self).__init__(id, floatingRateIndex, indexTenor, floatingRateMultiplierSchedule, spreadSchedule, rateTreatment, capRateSchedule, floorRateSchedule, capFloorStraddle, extensiontype_, )
supermod.FloatingRate.subclass = FloatingRateSub
# end class FloatingRateSub


class EuropeanExerciseSub(supermod.EuropeanExercise):
    def __init__(self, id=None, expirationDate=None, relevantUnderlyingDate=None, earliestExerciseTime=None, expirationTime=None, partialExercise=None, exerciseFee=None):
        super(EuropeanExerciseSub, self).__init__(id, expirationDate, relevantUnderlyingDate, earliestExerciseTime, expirationTime, partialExercise, exerciseFee, )
supermod.EuropeanExercise.subclass = EuropeanExerciseSub
# end class EuropeanExerciseSub


class DirectionalLegSub(supermod.DirectionalLeg):
    def __init__(self, id=None, legIdentifier=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, effectiveDate=None, terminationDate=None, extensiontype_=None):
        super(DirectionalLegSub, self).__init__(id, legIdentifier, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, effectiveDate, terminationDate, extensiontype_, )
supermod.DirectionalLeg.subclass = DirectionalLegSub
# end class DirectionalLegSub


class DeterminationMethodReferenceSub(supermod.DeterminationMethodReference):
    def __init__(self, href=None):
        super(DeterminationMethodReferenceSub, self).__init__(href, )
supermod.DeterminationMethodReference.subclass = DeterminationMethodReferenceSub
# end class DeterminationMethodReferenceSub


class DateReferenceSub(supermod.DateReference):
    def __init__(self, href=None):
        super(DateReferenceSub, self).__init__(href, )
supermod.DateReference.subclass = DateReferenceSub
# end class DateReferenceSub


class DateOffsetSub(supermod.DateOffset):
    def __init__(self, id=None, periodMultiplier=None, period=None, dayType=None, businessDayConvention=None):
        super(DateOffsetSub, self).__init__(id, periodMultiplier, period, dayType, businessDayConvention, )
supermod.DateOffset.subclass = DateOffsetSub
# end class DateOffsetSub


class CalculationPeriodFrequencySub(supermod.CalculationPeriodFrequency):
    def __init__(self, id=None, periodMultiplier=None, period=None, rollConvention=None):
        super(CalculationPeriodFrequencySub, self).__init__(id, periodMultiplier, period, rollConvention, )
supermod.CalculationPeriodFrequency.subclass = CalculationPeriodFrequencySub
# end class CalculationPeriodFrequencySub


class BusinessUnitReferenceSub(supermod.BusinessUnitReference):
    def __init__(self, href=None):
        super(BusinessUnitReferenceSub, self).__init__(href, )
supermod.BusinessUnitReference.subclass = BusinessUnitReferenceSub
# end class BusinessUnitReferenceSub


class BusinessDayAdjustmentsReferenceSub(supermod.BusinessDayAdjustmentsReference):
    def __init__(self, href=None):
        super(BusinessDayAdjustmentsReferenceSub, self).__init__(href, )
supermod.BusinessDayAdjustmentsReference.subclass = BusinessDayAdjustmentsReferenceSub
# end class BusinessDayAdjustmentsReferenceSub


class BusinessDateRangeSub(supermod.BusinessDateRange):
    def __init__(self, unadjustedFirstDate=None, unadjustedLastDate=None, businessDayConvention=None, businessCentersReference=None, businessCenters=None):
        super(BusinessDateRangeSub, self).__init__(unadjustedFirstDate, unadjustedLastDate, businessDayConvention, businessCentersReference, businessCenters, )
supermod.BusinessDateRange.subclass = BusinessDateRangeSub
# end class BusinessDateRangeSub


class BusinessCentersReferenceSub(supermod.BusinessCentersReference):
    def __init__(self, href=None):
        super(BusinessCentersReferenceSub, self).__init__(href, )
supermod.BusinessCentersReference.subclass = BusinessCentersReferenceSub
# end class BusinessCentersReferenceSub


class BermudaExerciseSub(supermod.BermudaExercise):
    def __init__(self, id=None, bermudaExerciseDates=None, relevantUnderlyingDate=None, earliestExerciseTime=None, latestExerciseTime=None, expirationTime=None, multipleExercise=None, exerciseFeeSchedule=None):
        super(BermudaExerciseSub, self).__init__(id, bermudaExerciseDates, relevantUnderlyingDate, earliestExerciseTime, latestExerciseTime, expirationTime, multipleExercise, exerciseFeeSchedule, )
supermod.BermudaExercise.subclass = BermudaExerciseSub
# end class BermudaExerciseSub


class AmountScheduleSub(supermod.AmountSchedule):
    def __init__(self, id=None, initialValue=None, step=None, currency=None):
        super(AmountScheduleSub, self).__init__(id, initialValue, step, currency, )
supermod.AmountSchedule.subclass = AmountScheduleSub
# end class AmountScheduleSub


class AmountReferenceSub(supermod.AmountReference):
    def __init__(self, href=None):
        super(AmountReferenceSub, self).__init__(href, )
supermod.AmountReference.subclass = AmountReferenceSub
# end class AmountReferenceSub


class AmericanExerciseSub(supermod.AmericanExercise):
    def __init__(self, id=None, commencementDate=None, expirationDate=None, relevantUnderlyingDate=None, earliestExerciseTime=None, latestExerciseTime=None, expirationTime=None, multipleExercise=None, exerciseFeeSchedule=None):
        super(AmericanExerciseSub, self).__init__(id, commencementDate, expirationDate, relevantUnderlyingDate, earliestExerciseTime, latestExerciseTime, expirationTime, multipleExercise, exerciseFeeSchedule, )
supermod.AmericanExercise.subclass = AmericanExerciseSub
# end class AmericanExerciseSub


class AccountReferenceSub(supermod.AccountReference):
    def __init__(self, href=None):
        super(AccountReferenceSub, self).__init__(href, )
supermod.AccountReference.subclass = AccountReferenceSub
# end class AccountReferenceSub


class UnderlyerReferenceSub(supermod.UnderlyerReference):
    def __init__(self, href=None):
        super(UnderlyerReferenceSub, self).__init__(href, )
supermod.UnderlyerReference.subclass = UnderlyerReferenceSub
# end class UnderlyerReferenceSub


class GenericResetFrequencySub(supermod.GenericResetFrequency):
    def __init__(self, id=None, periodMultiplier=None, period=None, underlyerReference=None):
        super(GenericResetFrequencySub, self).__init__(id, periodMultiplier, period, underlyerReference, )
supermod.GenericResetFrequency.subclass = GenericResetFrequencySub
# end class GenericResetFrequencySub


class GenericOptionStrikeSub(supermod.GenericOptionStrike):
    def __init__(self, strikePrice=None, strikePercentage=None, strikeDeterminationDate=None, currency=None, units=None):
        super(GenericOptionStrikeSub, self).__init__(strikePrice, strikePercentage, strikeDeterminationDate, currency, units, )
supermod.GenericOptionStrike.subclass = GenericOptionStrikeSub
# end class GenericOptionStrikeSub


class GenericProductSub(supermod.GenericProduct):
    def __init__(self, id=None, primaryAssetClass=None, secondaryAssetClass=None, productType=None, productId=None, assetClass=None, embeddedOptionType=None, multiLeg=None, buyerPartyReference=None, buyerAccountReference=None, sellerPartyReference=None, sellerAccountReference=None, counterpartyReference=None, premium=None, effectiveDate=None, expirationDate=None, terminationDate=None, underlyer=None, notional=None, grade=None, settlementPeriods=None, loadType=None, quantity=None, quantityFrequency=None, fixedPrice=None, interconnectionPoint=None, optionEntitlement=None, numberOfOptions=None, optionType=None, commencementDate=None, exerciseStyle=None, strike=None, feature=None, paymentFrequency=None, resetFrequency=None, settlementCurrency=None, settlementType=None):
        super(GenericProductSub, self).__init__(id, primaryAssetClass, secondaryAssetClass, productType, productId, assetClass, embeddedOptionType, multiLeg, buyerPartyReference, buyerAccountReference, sellerPartyReference, sellerAccountReference, counterpartyReference, premium, effectiveDate, expirationDate, terminationDate, underlyer, notional, grade, settlementPeriods, loadType, quantity, quantityFrequency, fixedPrice, interconnectionPoint, optionEntitlement, numberOfOptions, optionType, commencementDate, exerciseStyle, strike, feature, paymentFrequency, resetFrequency, settlementCurrency, settlementType, )
supermod.GenericProduct.subclass = GenericProductSub
# end class GenericProductSub


class GenericFrequencySub(supermod.GenericFrequency):
    def __init__(self, id=None, periodMultiplier=None, period=None, payerPartyReference=None, underlyerReference=None):
        super(GenericFrequencySub, self).__init__(id, periodMultiplier, period, payerPartyReference, underlyerReference, )
supermod.GenericFrequency.subclass = GenericFrequencySub
# end class GenericFrequencySub


class ReturnSwapLegUnderlyerSub(supermod.ReturnSwapLegUnderlyer):
    def __init__(self, id=None, legIdentifier=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, effectiveDate=None, terminationDate=None, strikeDate=None, underlyer=None, settlementType=None, settlementDate=None, settlementAmount=None, settlementCurrency=None, extensiontype_=None):
        super(ReturnSwapLegUnderlyerSub, self).__init__(id, legIdentifier, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, effectiveDate, terminationDate, strikeDate, underlyer, settlementType, settlementDate, settlementAmount, settlementCurrency, extensiontype_, )
supermod.ReturnSwapLegUnderlyer.subclass = ReturnSwapLegUnderlyerSub
# end class ReturnSwapLegUnderlyerSub


class ReturnLegSub(supermod.ReturnLeg):
    def __init__(self, id=None, legIdentifier=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, effectiveDate=None, terminationDate=None, strikeDate=None, underlyer=None, settlementType=None, settlementDate=None, settlementAmount=None, settlementCurrency=None, rateOfReturn=None, notional=None, amount=None, return_=None, notionalAdjustments=None, fxFeature=None, averagingDates=None):
        super(ReturnLegSub, self).__init__(id, legIdentifier, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, effectiveDate, terminationDate, strikeDate, underlyer, settlementType, settlementDate, settlementAmount, settlementCurrency, rateOfReturn, notional, amount, return_, notionalAdjustments, fxFeature, averagingDates, )
supermod.ReturnLeg.subclass = ReturnLegSub
# end class ReturnLegSub


class InterestLegSub(supermod.InterestLeg):
    def __init__(self, id=None, legIdentifier=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, effectiveDate=None, terminationDate=None, interestLegCalculationPeriodDates=None, notional=None, interestAmount=None, interestCalculation=None, stubCalculationPeriod=None):
        super(InterestLegSub, self).__init__(id, legIdentifier, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, effectiveDate, terminationDate, interestLegCalculationPeriodDates, notional, interestAmount, interestCalculation, stubCalculationPeriod, )
supermod.InterestLeg.subclass = InterestLegSub
# end class InterestLegSub


class DirectionalLegUnderlyerSub(supermod.DirectionalLegUnderlyer):
    def __init__(self, id=None, legIdentifier=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, effectiveDate=None, terminationDate=None, underlyer=None, settlementType=None, settlementDate=None, settlementAmount=None, settlementCurrency=None, fxFeature=None, extensiontype_=None):
        super(DirectionalLegUnderlyerSub, self).__init__(id, legIdentifier, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, effectiveDate, terminationDate, underlyer, settlementType, settlementDate, settlementAmount, settlementCurrency, fxFeature, extensiontype_, )
supermod.DirectionalLegUnderlyer.subclass = DirectionalLegUnderlyerSub
# end class DirectionalLegUnderlyerSub


class FxValuationDateOffsetSub(supermod.FxValuationDateOffset):
    def __init__(self, id=None, periodMultiplier=None, period=None, dayType=None, businessCentersReference=None, businessCenters=None):
        super(FxValuationDateOffsetSub, self).__init__(id, periodMultiplier, period, dayType, businessCentersReference, businessCenters, )
supermod.FxValuationDateOffset.subclass = FxValuationDateOffsetSub
# end class FxValuationDateOffsetSub


class FxOptionPremiumSub(supermod.FxOptionPremium):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentDate=None, paymentAmount=None, settlementInformation=None, quote=None):
        super(FxOptionPremiumSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentDate, paymentAmount, settlementInformation, quote, )
supermod.FxOptionPremium.subclass = FxOptionPremiumSub
# end class FxOptionPremiumSub


class ClassifiablePaymentSub(supermod.ClassifiablePayment):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentDate=None, paymentAmount=None, paymentType=None):
        super(ClassifiablePaymentSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentDate, paymentAmount, paymentType, )
supermod.ClassifiablePayment.subclass = ClassifiablePaymentSub
# end class ClassifiablePaymentSub


class CommoditySpreadSub(supermod.CommoditySpread):
    def __init__(self, id=None, currency=None, amount=None, spreadConversionFactor=None, spreadUnit=None):
        super(CommoditySpreadSub, self).__init__(id, currency, amount, spreadConversionFactor, spreadUnit, )
supermod.CommoditySpread.subclass = CommoditySpreadSub
# end class CommoditySpreadSub


class CommodityPremiumSub(supermod.CommodityPremium):
    def __init__(self, id=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, paymentDate=None, paymentAmount=None, premiumPerUnit=None):
        super(CommodityPremiumSub, self).__init__(id, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, paymentDate, paymentAmount, premiumPerUnit, )
supermod.CommodityPremium.subclass = CommodityPremiumSub
# end class CommodityPremiumSub


class FutureSub(supermod.Future):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, relatedExchangeId=None, optionsExchangeId=None, specifiedExchangeId=None, multiplier=None, futureContractReference=None, maturity=None, contractYearMonth=None):
        super(FutureSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, relatedExchangeId, optionsExchangeId, specifiedExchangeId, multiplier, futureContractReference, maturity, contractYearMonth, )
supermod.Future.subclass = FutureSub
# end class FutureSub


class ExchangeTradedContractSub(supermod.ExchangeTradedContract):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, relatedExchangeId=None, optionsExchangeId=None, specifiedExchangeId=None, multiplier=None, contractReference=None, expirationDate=None, extensiontype_=None):
        super(ExchangeTradedContractSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, relatedExchangeId, optionsExchangeId, specifiedExchangeId, multiplier, contractReference, expirationDate, extensiontype_, )
supermod.ExchangeTradedContract.subclass = ExchangeTradedContractSub
# end class ExchangeTradedContractSub


class ExchangeTradedCalculatedPriceSub(supermod.ExchangeTradedCalculatedPrice):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, relatedExchangeId=None, optionsExchangeId=None, specifiedExchangeId=None, constituentExchangeId=None, extensiontype_=None):
        super(ExchangeTradedCalculatedPriceSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, relatedExchangeId, optionsExchangeId, specifiedExchangeId, constituentExchangeId, extensiontype_, )
supermod.ExchangeTradedCalculatedPrice.subclass = ExchangeTradedCalculatedPriceSub
# end class ExchangeTradedCalculatedPriceSub


class ConvertibleBondSub(supermod.ConvertibleBond):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, issuerName=None, issuerPartyReference=None, seniority=None, couponType=None, couponRate=None, maturity=None, parValue=None, faceAmount=None, paymentFrequency=None, dayCountFraction=None, underlyingEquity=None, redemptionDate=None):
        super(ConvertibleBondSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, issuerName, issuerPartyReference, seniority, couponType, couponRate, maturity, parValue, faceAmount, paymentFrequency, dayCountFraction, underlyingEquity, redemptionDate, )
supermod.ConvertibleBond.subclass = ConvertibleBondSub
# end class ConvertibleBondSub


class UnderlyerInterestLegSub(supermod.UnderlyerInterestLeg):
    def __init__(self, id=None, legIdentifier=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, effectiveDate=None, terminationDate=None, fixedRate=None, spreadSchedule=None):
        super(UnderlyerInterestLegSub, self).__init__(id, legIdentifier, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, effectiveDate, terminationDate, fixedRate, spreadSchedule, )
supermod.UnderlyerInterestLeg.subclass = UnderlyerInterestLegSub
# end class UnderlyerInterestLegSub


class RelativeDateOffsetSub(supermod.RelativeDateOffset):
    def __init__(self, id=None, periodMultiplier=None, period=None, dayType=None, businessDayConvention=None, businessCentersReference=None, businessCenters=None, dateRelativeTo=None, adjustedDate=None, extensiontype_=None):
        super(RelativeDateOffsetSub, self).__init__(id, periodMultiplier, period, dayType, businessDayConvention, businessCentersReference, businessCenters, dateRelativeTo, adjustedDate, extensiontype_, )
supermod.RelativeDateOffset.subclass = RelativeDateOffsetSub
# end class RelativeDateOffsetSub


class FloatingRateCalculationSub(supermod.FloatingRateCalculation):
    def __init__(self, id=None, floatingRateIndex=None, indexTenor=None, floatingRateMultiplierSchedule=None, spreadSchedule=None, rateTreatment=None, capRateSchedule=None, floorRateSchedule=None, capFloorStraddle=None, initialRate=None, finalRateRounding=None, averagingMethod=None, negativeInterestRateTreatment=None):
        super(FloatingRateCalculationSub, self).__init__(id, floatingRateIndex, indexTenor, floatingRateMultiplierSchedule, spreadSchedule, rateTreatment, capRateSchedule, floorRateSchedule, capFloorStraddle, initialRate, finalRateRounding, averagingMethod, negativeInterestRateTreatment, )
supermod.FloatingRateCalculation.subclass = FloatingRateCalculationSub
# end class FloatingRateCalculationSub


class AdjustedRelativeDateOffsetSub(supermod.AdjustedRelativeDateOffset):
    def __init__(self, id=None, periodMultiplier=None, period=None, dayType=None, businessDayConvention=None, businessCentersReference=None, businessCenters=None, dateRelativeTo=None, adjustedDate=None, relativeDateAdjustments=None):
        super(AdjustedRelativeDateOffsetSub, self).__init__(id, periodMultiplier, period, dayType, businessDayConvention, businessCentersReference, businessCenters, dateRelativeTo, adjustedDate, relativeDateAdjustments, )
supermod.AdjustedRelativeDateOffset.subclass = AdjustedRelativeDateOffsetSub
# end class AdjustedRelativeDateOffsetSub


class DirectionalLegUnderlyerValuationSub(supermod.DirectionalLegUnderlyerValuation):
    def __init__(self, id=None, legIdentifier=None, payerPartyReference=None, payerAccountReference=None, receiverPartyReference=None, receiverAccountReference=None, effectiveDate=None, terminationDate=None, underlyer=None, settlementType=None, settlementDate=None, settlementAmount=None, settlementCurrency=None, fxFeature=None, valuation=None):
        super(DirectionalLegUnderlyerValuationSub, self).__init__(id, legIdentifier, payerPartyReference, payerAccountReference, receiverPartyReference, receiverAccountReference, effectiveDate, terminationDate, underlyer, settlementType, settlementDate, settlementAmount, settlementCurrency, fxFeature, valuation, )
supermod.DirectionalLegUnderlyerValuation.subclass = DirectionalLegUnderlyerValuationSub
# end class DirectionalLegUnderlyerValuationSub


class IndexSub(supermod.Index):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, relatedExchangeId=None, optionsExchangeId=None, specifiedExchangeId=None, constituentExchangeId=None, futureId=None):
        super(IndexSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, relatedExchangeId, optionsExchangeId, specifiedExchangeId, constituentExchangeId, futureId, )
supermod.Index.subclass = IndexSub
# end class IndexSub


class ExchangeTradedOptionSub(supermod.ExchangeTradedOption):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, relatedExchangeId=None, optionsExchangeId=None, specifiedExchangeId=None, multiplier=None, contractReference=None, expirationDate=None, strike=None, optionType=None):
        super(ExchangeTradedOptionSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, relatedExchangeId, optionsExchangeId, specifiedExchangeId, multiplier, contractReference, expirationDate, strike, optionType, )
supermod.ExchangeTradedOption.subclass = ExchangeTradedOptionSub
# end class ExchangeTradedOptionSub


class ExchangeTradedFundSub(supermod.ExchangeTradedFund):
    def __init__(self, id=None, instrumentId=None, description=None, currency=None, exchangeId=None, clearanceSystem=None, definition=None, relatedExchangeId=None, optionsExchangeId=None, specifiedExchangeId=None, constituentExchangeId=None, fundManager=None):
        super(ExchangeTradedFundSub, self).__init__(id, instrumentId, description, currency, exchangeId, clearanceSystem, definition, relatedExchangeId, optionsExchangeId, specifiedExchangeId, constituentExchangeId, fundManager, )
supermod.ExchangeTradedFund.subclass = ExchangeTradedFundSub
# end class ExchangeTradedFundSub


class RelativeDatesSub(supermod.RelativeDates):
    def __init__(self, id=None, periodMultiplier=None, period=None, dayType=None, businessDayConvention=None, businessCentersReference=None, businessCenters=None, dateRelativeTo=None, adjustedDate=None, periodSkip=None, scheduleBounds=None):
        super(RelativeDatesSub, self).__init__(id, periodMultiplier, period, dayType, businessDayConvention, businessCentersReference, businessCenters, dateRelativeTo, adjustedDate, periodSkip, scheduleBounds, )
supermod.RelativeDates.subclass = RelativeDatesSub
# end class RelativeDatesSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'GenericCommodityDeliveryPeriod'
        rootClass = supermod.GenericCommodityDeliveryPeriod
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'GenericCommodityDeliveryPeriod'
        rootClass = supermod.GenericCommodityDeliveryPeriod
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'GenericCommodityDeliveryPeriod'
        rootClass = supermod.GenericCommodityDeliveryPeriod
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'GenericCommodityDeliveryPeriod'
        rootClass = supermod.GenericCommodityDeliveryPeriod
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from fpml01/fpml_genericlib import *\n\n')
        sys.stdout.write('import fpml01/fpml_genericlib as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
