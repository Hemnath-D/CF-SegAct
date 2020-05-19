
import config as cfg
import glob
import json
import os
import requests
import time


def extractProblemCodes(response):
    """ Method extractProblemCodes(response) - Returns the list Problem Codes by parsing the json response"""
    # 1. Get all the problem codes with verdict "OK" in response
    submissions = response['result']
    problem_codes = []
    for submission in submissions:
        verdict = submission['verdict']
        problem = submission['problem']
        if verdict == "OK":
            problem_codes.append(str(problem['contestId']) + problem['index'])
    return problem_codes

def getProblemCodes(handle, max_submissions):
    """ Method getProblemCodes(handle, max_submissions) - Returns the list of AC problem codes from Codeforces API"""
    # 1. Get the API response using user.status method in codeforces api
    # 2. Extract the problem codes of AC submissions from the response
    url = url = "https://codeforces.com/api/user.status?handle=" + handle + "&count=" + str(max_submissions)
    response = requests.get(url).json()
    return extractProblemCodes(response)

# Method getMatchingFiles(sol_dir, problem_codes) - Returns the list of 
def getMatchingFiles(sol_dir, problem_codes):
    """ Method getMatchingFiles(sol_dir, problem_codes) - Returns the list of matching files matching the problem_codes"""
    # 1. Change the directory to sol_dir
    # 2. Get the files matching the problem_codes using regex
    os.chdir(sol_dir)
    matching_files = []
    for problem_code in problem_codes:
        matching_files.extend(glob.glob(problem_code+"*"))
    return matching_files

def moveMatchingFiles(sol_dir, dest_dir, matching_files):
    """Method moveMatchingFiles(sol_dir, dest_dir, matching_files) Move all the files from matching_files to dest_dir"""
    for matching_file in matching_files:
        os.rename(sol_dir + "/" + matching_file, dest_dir + "/" + matching_file)
    print(str(len(matching_files)) + " file(s) moved to " + dest_dir + " from " + sol_dir)

def segFiles():
    """Method segFiles() - Moves the AC files from solutions directory to the destination directory"""
    #1. Get all solved Problem Codes using codeforces API
    problem_codes = getProblemCodes(cfg.HANDLE, cfg.MAX_SUBMISSIONS)
    #2. Get the list of all solution files in local system which matches the
    #retrieved Problem Code
    matching_files = getMatchingFiles(cfg.SOL_DIR, problem_codes)
    #3. Move the files to the DEST_DIR
    moveMatchingFiles(cfg.SOL_DIR, cfg.DEST_DIR, matching_files)
    
def runAtInterval():
    """ Method runAtInterval() - Run the code at the user specified intervals"""
    while True:
        segFiles()
        time.sleep(cfg.INTERVAL)

runAtInterval()