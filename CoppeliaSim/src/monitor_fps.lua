-- Initialize the required variables
local previousRealTime = sim.getSystemTime()
local frameCount = 0
local totalFrames = 0
local totalTime = 0
local runTime = 60 -- Specifies how long to run the monitoring in seconds

-- Start a loop to simulate frame counting
local startTime = sim.getSystemTime()
while (sim.getSystemTime() - startTime) < runTime do
    -- Simulate a frame increment
    frameCount = frameCount + 1
    sim.switchThread() -- This is crucial to prevent freezing CoppeliaSim

    -- Check time elapsed
    local currentRealTime = sim.getSystemTime()
    local elapsedRealTime = currentRealTime - previousRealTime

    -- Update every second
    if elapsedRealTime >= 1 then
        -- Calculate FPS
        local fps = frameCount / elapsedRealTime

        -- Print FPS
        print(string.format("FPS: %.2f", fps))

        -- Update counters and time stamps
        previousRealTime = currentRealTime
        totalFrames = totalFrames + frameCount
        totalTime = totalTime + elapsedRealTime
        frameCount = 0
    end
end

-- Print average FPS over the entire run period
print(string.format("Average FPS: %.2f", totalFrames / totalTime))
