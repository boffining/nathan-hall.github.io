from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import auc, roc_curve
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate
plt.style.use('fivethirtyeight')

def evaluate_features(features, model_feature_importances, model_title, width, height):
    #Extract the features for plotting
    importance_column_title = 'Importance'+model_title
    df_features = pd.DataFrame(columns=['Features', importance_column_title])
    df_features['Features'] = features
    df_features[importance_column_title] = model_feature_importances
    df_features.sort_values(importance_column_title, ascending=False, inplace=True)
    #Plot the most important features.
    plt.subplots(figsize=(width, height))
    sns.barplot(x=importance_column_title, y='Features', data=df_features)

def evaluate_classifier(X_test, y_test, y_pred, y_proba, chart_title):
    #Confusion matrix on test set
    cm = confusion_matrix(y_test, y_pred)
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    #Classification report on test set
    report = classification_report(y_test, y_pred).split()
    report = [float(i) for i in (report[4:9]+report[9:14]+report[17:20])]
    #Chart title
    print " "
    print "%s" % chart_title
    print " "
    #Setup the subplots
    f, (ax1, ax2) = plt.subplots(1, 2, gridspec_kw = {'width_ratios':[1, 1]}, figsize=(10, 4))
    #Build the confusion matrix
    sns.heatmap(cm_normalized, annot=True, ax=ax1)
    ax1.set_title('Confusion Matrix')
    ax1.set_ylabel('True')
    ax1.set_xlabel('Pred')
    #Build the roc_auc score
    fpr, tpr, thresholds = roc_curve(y_test, y_proba[:,1])
    roc_auc = auc(fpr, tpr)
    ax2.plot(fpr, tpr, label='%s (area = %0.2f)' % (chart_title, roc_auc), linewidth=4)
    ax2.plot([0, 1], [0, 1], 'k--', linewidth=4)
    ax2.set_title('ROC_AUC Score')
    ax2.set_xlim([0.0, 1.0])
    ax2.set_ylim([0.0, 1.05])
    ax2.set_xlabel('False Positive Rate', fontsize=18)
    ax2.set_ylabel('True Positive Rate', fontsize=18)
    ax2.legend(loc="lower right")
    plt.show()
    cf_title = 'CONFUSTION MATRIX'
    cf_subtitle = '(n = %0.0f)' % len(X_test)
    cf_table_headers = ['positives', 'negatives']
    cf_dict = {
        'positives' : ['TP = %0.0f' % cm[0,0], 'FP = %0.0f' % cm[1,0]],
        'negatives' : ['FN = %0.0f' % cm[0,1], 'TN = %0.0f' % cm[1,1]],
    }
    cl_title = 'CLASSIFICATION REPORT'
    cl_subtitle = 'n = (%0.0f = %0.0f) (%0.0f = %0.0f)' % (report[0], report[4], report[5], report[9])
    cl_table_headers = [' ', '%0.0f' % report[0], '%0.0f' % report[5], 'avg']
    cl_dict = {
        'category' : ['precision', 'recall', 'f1-score', 'total_avg'],
        '0' : ['%0.2f' % report[1], '%0.2f' % report[2], '%0.2f' % report[3], '%0.2f' % (sum(report[1:4])/3.0)],
        '1' :  ['%0.2f' % report[6], '%0.2f' % report[7], '%0.2f' % report[8], '%0.2f' % (sum(report[6:9])/3.0)],
        'avg' :  ['%0.2f' % report[10], '%0.2f' % report[11], '%0.2f' % report[12], '%0.2f' % (sum(report[10:13])/3.0)],
    }
    print cf_title
    print cf_subtitle
    print tabulate(cf_dict, cf_table_headers, tablefmt="rst")
    print " "
    print " "
    print cl_title
    print cl_subtitle
    print tabulate(cl_dict, cl_table_headers, tablefmt="rst")
